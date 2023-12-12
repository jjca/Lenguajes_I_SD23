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





##### 1.iii Describa el mecanismo de sincronización que utiliza el lenguaje

