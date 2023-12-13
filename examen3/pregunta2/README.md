# Pregunta 2

Se usó el lenguaje de programación Julia. Para ejecutar el código, se debe descargar el [código fuente](https://julialang.org/downloads/) y exraer el comprimido. Dentro habrá un ejecutable para poder ejecutar el código.

Esta implementación está hecha para trabajar con hilos, de forma que se recomienda ejecutar: `julia -t 4 productoPunto.jl`.

Para notar la diferencia en el tiempo es necesario que el n sea grande, actualmente está establecido en $n = 10.000.000$. Se debe tener cuidado de no quedarse sin memoria durante al ejecución.

La función `productoPuntoPF` usa sumas atómicas. La función `productoPuntoD` usa una suma distribuida maneajda por la librería `Distributed`

Hay una implementación iterativa sin paralelismo para confirmar el cálculo así como comparar el tiempo de ejecución, el cual puede reducirse en 3 veces el tiempo de la ejecución secuencial.


Comentarios:

- La función `productoPuntoP(x,y)` funciona para números enteros y punto flotante. La implementación actual sirve para casos de punto flotante. Esta función también da valores correctos con múltiples procesos y múltiples hilos: `julia -p 2 -t 6`.
- La función `productoPuntoD(x,y)` funciona correctamente para números enteros si se usan varios procesos `julia -p 2`. Si se usan únicamente varios hilos `julia -t 6`, la función devuelve el valor correcto para enteros y punto flotante.


```Bash
jorge@Sorna:~$ julia -t 8 productoPunto.jl 
Número de hilos: 8
Punto flotante
productoPuntoPF 2.5008974852093705e6
  0.886400 seconds (74.59 k allocations: 5.247 MiB, 33.54% compilation time)
productoPunto 2.5008974852094096e6
  1.273235 seconds (70.00 M allocations: 1.192 GiB, 3.29% gc time, 1.72% compilation time)
productoPuntoD 2.5008974852094096e6
  0.534804 seconds (30.15 M allocations: 468.196 MiB, 3.03% gc time, 25.55% compilation time)
Enteros
productoPuntoPE 249996221540871
  0.215013 seconds (37.72 k allocations: 2.600 MiB, 80.91% compilation time)
productoPunto 249996221540871
  1.322175 seconds (68.98 M allocations: 1.177 GiB, 3.98% gc time, 0.90% compilation time)
productoPuntoD 249996221540871
  0.462304 seconds (30.03 M allocations: 459.908 MiB, 1.61% gc time, 9.87% compilation time)
```

Se puede observar que los casos paralelos tienen menor consumo de memoria y de tiempo. El resultado de `productoPuntoPF` posee un margen de error entre el resultado distribuido. Es posible se deba a errores a nivel de procesador.

Si se ejecuta `julia -p 2 -t 4` por ejemplo, la función `productoPuntoD` arroja 0. Probablemente debido a una condición de carrera de dos procesos

```Bash
jorge@Sorna:~$ julia -t 4 -p 2 productoPunto.jl 
Número de hilos: 4
Punto flotante
productoPuntoPF 2.501004113694023e6
  0.770841 seconds (73.92 k allocations: 5.031 MiB, 22.86% compilation time)
productoPunto 2.501004113694519e6
  1.177998 seconds (70.08 M allocations: 1.198 GiB, 3.68% gc time, 9.48% compilation time)
productoPuntoD 0
  1.211847 seconds (675.76 k allocations: 45.150 MiB, 0.44% gc time, 42.29% compilation time)
Enteros
productoPuntoPE 250080247523476
  0.207989 seconds (37.60 k allocations: 2.587 MiB, 45.79% compilation time)
productoPunto 250080247523476
  1.221682 seconds (68.98 M allocations: 1.177 GiB, 2.27% gc time, 0.96% compilation time)
productoPuntoD 0
  0.362791 seconds (25.76 k allocations: 1.744 MiB, 7.45% compilation time)
```