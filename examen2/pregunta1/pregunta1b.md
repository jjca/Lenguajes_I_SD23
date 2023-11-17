# Se tienen los siguientes comentarios sobre las preguntas `1bi` y `1bii`

## Pregunta 1bi

Se definieron los "números" `cero, uno, dos, tres, cuatro, cinco, seis, siete`. El caso base es el "número" `cero`, y todos los demás fueron construidos usando la función `sucesor` sobre cada número. Esto es, para construir al `uno` se tiene `suc(cero) = uno`.

Luego, la definición recursiva de cada número es:

```
cero
uno = suc(cero)
dos = suc(uno) = suc(suc(cero))
tres = suc(dos) = suc(suc(uno)) = suc(suc(suc(cero)))
```

La representación "extendida" es lo que imprime el programa, esto es, para el caso de tres es: $suc(suc(suc(cero)))$

Existe un error (no determinado) para la impresión de la expresión extendida del "número", donde cada 3 paréntesis aparece un `!`. Esto no tengo idea por qué pasa, probablemente se deba a temas de accesos de memoria en C.

## Pregunta 1bii

Luego de pruebas, se ve que un _max-heap simétrico_ sólo ocurre en dos casos:
1. El árbol está formado únicamente por un nodo.
2. Todos los valores de los nodos son iguales.

Esto considerando que el recorrido es el orden en el que van apareciendo los vlaores de los nodos.

Los dos casos mostrados previamente se mencionan en el código, así como un tercer caso que NO es un _max-heap simétrico_.