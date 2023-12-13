# Pregunta 2

Se usó el lenguaje de programación Julia. Para ejecutar el código, se debe descargar el [código fuente](https://julialang.org/downloads/) y exraer el comprimido. Dentro habrá un ejecutable para poder ejecutar el código.

Esta implementación está hecha para trabajar con hilos, de forma que se recomienda ejecutar: `julia -t 4 productoPunto.jl`.

Para notar la diferencia en el tiempo es necesario que el n sea grande, actualmente está establecido en $n = 100.000.000$. Se debe tener cuidado de no quedarse sin memoria durante al ejecución.

Hay una implementación iterativa sin paralelismo para confirmar el cálculo así como comparar el tiempo de ejecución, el cual puede reducirse en 3 veces el tiempo de la ejecución secuencial.
