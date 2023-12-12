```Haskell
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr _ e [] = e
foldr f e (x:xs) = f x $ foldr f e xs


const :: a -> b -> a
const x _ = x
```

Considere también la siguiente función que aplica una función solamente sobre la cola de una lista y agrupa la cabeza con otro valor dado:
```Haskell
what :: a -> ([b] -> [(a, b)]) -> [b] -> [(a, b)]
what _ _ [] = []
what x f (y:ys) = (x, y) : f ys
```

(a) Considere la siguiente implementación de una función misteriosa, usando foldr:
```Haskell
misteriosa :: ???
misteriosa = foldr what (const [])
```
Considere también la siguiente función, que genera una lista de números enteros a partir de un cierto valor inicial:
```
gen :: Int -> [Int]
gen n = n : gen (n + 1)
```
Muestre la evaluación, paso a paso, de la expresión misteriosa "abc" (gen 1), considerando que:
i. El lenguaje tiene orden de evaluación normal.

Caso cuando el lengauje tiene evaluación normal:

```
misteriosa "abc" (gen 1)
```


ii. El lenguaje tiene orden de evaluación aplicativo.
(b) Considere el siguiente tipo de datos que representa árboles binarios con información
en las ramas:
data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)
Construya una función foldA (junto con su firma) que permita reducir un valor de
tipo (Arbol a) a algún tipo b (de forma análoga a foldr). Su implementación debe
poder tratar con estructuras potencialmente infinitas.
Su función debe cumplir con la siguiente firma:
foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
6(c) Considere una versión de la función what que funciona sobre árboles (aplica la función
proporcionada a ambos sub–árboles) y llamésmola what tree function:
whatTF :: a
-> (Arbol b -> Arbol (a, b))
-> (Arbol b -> Arbol (a, b))
-> Arbol b
-> Arbol (a, b)
whatTF _ _ _ Hoja
= Hoja
whatTF x f g (Rama y i d) = Rama (x, y) (f i) (g d)
Usando su función foldA definimos la función sospechosa:
sospechosa :: ???
sospechosa = foldA whatTF (const Hoja)
Definimos también la siguiente función, que genera un árbol de números enteros a
partir de un cierto valor inicial:
genA :: Int -> Arbol Int
genA n = Rama n (genA (n + 1)) (genA (n * 2))
Finalmente, definimos el valor arbolito como una instancia de Arbol Char:
arbolito :: Arbol Char
arbolito = Rama 'a' (Rama 'b' Hoja (Rama 'c' Hoja Hoja)) Hoja
Muestre la evaluación, paso a paso, de la expresión sospechosa arbolito (genA 1),
considerando que:
i. El lenguaje tiene orden de evaluación normal.
ii. El lenguaje tiene orden de evaluación aplicativo.
Si sospecha que en algún momento uno de estos programas puede caer en una evaluación
recursiva infinita, realice las primeras expansiones, detenga la evaluación y argumente las
razones por las que cree que dicha evaluación no terminaría.