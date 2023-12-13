# Pregunta 5

Muestre la evaluación, paso a paso, de la expresión `misteriosa "abc" (gen 1)`, considerando que:

1. El lenguaje tiene orden de evaluación normal. (Siendo lazy y de afuera hacia adentro)

```
misteriosa "abc" (gen 1)

<Evaluacion de misteriosa>

foldr what (const []) "abc" (gen 1)

<Aplicacion de foldr>

what "a" $ foldr what (const []) "bc" (1:gen 2)

<Definicion de what y gen>

("a",1) : foldr what (const []) "bc" (gen 2)

<Aplicacion de foldr>

("a",1) : what "b" $ foldr what (const []) "c" (gen 2)

<Definicion what y gen>

("a",1) : ("b",2) : foldr what (const []) "c" (gen 3)

<Aplicacion de foldr>

("a",1) : ("b",2) : what "c" $ foldr what (const []) [] (gen 3)

<Definicion de what y gen>

("a",1) : ("b",2) : ("c",3) : foldr what (const []) [] (gen 4)

<Aplicación de what>

("a",1) : ("b",2) : ("c",3) : const [] (gen 4)

<Definición de const>

("a",1) : ("b",2) : ("c",3) : []

<Concatenación de lista>

[("a",1),("b",2),("c",3)]
```

ii. El lenguaje tiene orden de evaluación aplicativo. (Evaluando antes de pasar y de adentro hacia afuera)

```Haskell
misteriosa "abc" (gen 1)

<Evaluación de gen>

misteriosa "abc" (1:gen 2)

<Evaluación de gen>

misteriosa "abc" (1:2:gen 3)
```

Va a terminar en un loop infinito debido a que la función `gen` seguirá generando números, debido a que al ser evaluación aplicativa, primero habría que terminar de evaluar todas las funciones internas antes de ir a evaluar a `misteriosa`, sin embargo esto no terminará nunca.