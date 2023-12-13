# Pregunta 2

Se escogió el lenguaje de programación Julia por sus capacidades de concurrencia, además de facilidad de programación y que es de propósito general. (Debí haberlo usado para el parcial 1 t.t)

#### 1. De una breve descripción de los mecanismos de concurrencia disponibles en su lenguaje

Julia posee de forma nativa los siguientes mecanismos para la concurrencia:

- Tareas asíncronas o corrutinas: permite suspender tareas, manejo de eventos, y sincronización mediante canales. Para esto se puede usar el módulo `@async`
- Multihilos: hacer tareas simultáneas en diferentes procesadores gracias al módulo `@Threads`. Es además posible definir la cantidad de hilos antes de ejecutar el programa con un flag.
- Computación distribuida: a nivel de diferentes computadoras y también diferentes espacios de memoria.
- Computación con GPU. permite ejecutar Julia directamente en GPUs.


##### 1.ii Diga si su lenguaje provee capacidades nativas para concurrencia, usa librerías o depende de herramientas externas

El lenguaje posee capacidades nativas para concurrencia, e igualente posee librerías extras para añadir mejores funcionalidades, como por ejemplo las incluidas en https://github.com/JuliaParallel. Aquí hay para manejo de MPI, arreglos distribuidos, clusterización, arreglos distribuidos, etc.

Es necesario ejecutar a Julia con el argumento -p (número de trabajadores) o -t (hilos). `julia -p 2` crea una consola interactiva de Julia con las librerías para poder ejecutar tareas en paralelo.

La cantidad de trabajadores corresponde con el número de subprocesos  a ser creados. Se tendrán realmente n+1, debido al proceso padre.

##### 1.ii Explique la creación/manejo de tareas concurrentes, así como el control de la memoria compartida y/o pasaje de mensajes

Para realizar tareas en paralelo se puede usar el módulo `@Threads`

Por ejemplo:

```Julia
function sum_single(a)
           s = 0
           for i in a
               s += i
           end
           s
       end
function sum_multi_good(a)
           chunks = Iterators.partition(a, length(a) ÷ Threads.nthreads())
           tasks = map(chunks) do chunk
               Threads.@spawn sum_single(chunk)
           end
           chunk_sums = fetch.(tasks)
           return sum_single(chunk_sums)
       end
julia > sum_multi_good(1:1_000_000)
```

En este caso, se tiene el iterador `chunks`, el cual segmenta la suma en chunks de acuerdo al largo del número así como de la cantidad de hilos disponibles. Con el módulo `Threads` se ejecuta la función `sum_single` por cada uno de estos chunks, almacenando el resultado en el mapa `tasks`.

El pasaje de mensajes en Julia no se hace como en otros casos con MPI (aunque hay una librería para ello). Más bien, es generalmente de "un solo lado" es decir, el programador explícitamente maneja un proceso en una operación de dos procesos. Es decir, no es enviar un mensaje y recibir un mensaje.

Esto se construye sobre _referencias remotas_ y _llamadas remotas_.

Una referencia remota es un objeto que puede usare desde cualquier proceso para referirse a un objeto almacenado en un proceso particular.

Una llamada remota, es una solicitud hecha por un proceso para llamar a otra función con ciertos argumentos en otro proceso, inclusive el mismo proceso.

Por ejemplo:

```Julia
addprocs(Sys.CPU_CORES - 1)
r1 = remotecall(rand,2,2,2)
r2 = remotecall(rand,2,1:8,3,4)
```

La sintaxis de `remotecall()` es: Función, ID del worker y los argumentos de la función. 

En este caso, la primera línea se llamó a la función `rand` la cual genera una matriz 2x2.

Para la segunda línea se usó igualmente `rand` asignando el trabajo al worker 2 para generar una matriz 3x4 con números entre 1 y 8.

Estas funciones generan un tipo de referencia remota llamado `Future`, el cual permite luego hacer consultas del resultado con `fetch()`. Sin embargo, esto sólo permite consultar mas no permite guardar o ver tipos. Es necesario asignarlo a otra variable:

```Julia
fetch(r1)
fetch(r2)

r1
r1[2,2]
typeof(r1)

r3 = fetch(r1)
typeof(r3)
sum(r3)
```

También es posible hacer uso de `@spawnat` el cual también retorna un `Future`.


Para el manejo de mensajes y de memoria compartida, se tiene:

- Aún cuando Julia no lo posee de forma nativa, existe un paquete llamado MPI.jl el cual permite implementar el estandar de MPI en Julia.
- Para la computación con memoria compartida están las `remote calls` y las `remote references`. También se tiene un arreglo distribuido, la implementación de la función `map` pero para hilos y el macro `@distributed`


##### 1.iii Describa el mecanismo de sincronización que utiliza el lenguaje

Para la sincronización y evitar condiciones de carrera, se usan `@sync`, los canales. 

El programador es responsable de que no ocurran condiciones de carrera. 