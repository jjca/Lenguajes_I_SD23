## Comentarios
Esta pregunta fue resuelta en tres hojas de papel. La última línea de la pila corresponde con el número 167.

Se especificaron las líneas del código de la siguiente forma:

```Python
     def misterio(a, b, c, d):
0  |    if c == 0:
1  |        yield a
2  |        for x in misterio(b, a, b, d - 1):
3  |            yield x
4  |    elif d > 0:
5  |        for x in misterio(a, b + 1, c - 1, d):
6  |            yield x

7  | a = 2 * X + 3 * Y + 2
8  | b = 4 * Y + 5 * Z + 1
9  | c = 5 * X + 2 * Z + 3
10 | d = (a + b + c) % 7
11 | for x in misterio(0, 1, 0, d + 1):
12 |    print x
```

Los valores para las constantes $X,Y,Z$ fueron: $X = 2$, $Y = 5$, $Z = 4$. Por lo tanto, los valores de $a,b,c,d$ son: $a = 21$, $b=41$, $c=21$ y $d = 6$.

La ejecución de las líneas $7,8,9,10$ no aparecen en el `pc` entregado, sin embargo aparecen enumeradas y pueden ser consideradas parte de la ejecución, aún cuando solo son ejecutadas una vez.