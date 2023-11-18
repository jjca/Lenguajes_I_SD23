# Pregunta 1a)
## Jorge Correia - 14-12054

Para responder esta pregunta se usó el lenguaje de programación C. Su elección además de seguir con el enunciado de la pregunta, es un lenguaje de programación con trayectoria, importancia y estabilidad.

- De una breve descripción del lenguaje escogido.
    1. Enumere y explique las estructuras de control de flujo que ofrece
    2. Diga en qué orden evalúan expresiones y funciones
    3. Diga qué tipos de datos posee y qué mecanismos ofrece para la creación de nuevos tipos (incluyendo tipos polimórficos de haberlos)
    4. Describa el funcionamiento del sistema de tipos del lenguaje, incluyendo el tipo de equivalencia para sus tipos, reglas de compatibilidad y capacidades de inferencias de tipos.

## Respuestas

### 1

Antes de continuar, es importante mencionar que C no posee un tipo de dato booleano. Para C, false es 0 y true cualquier número entero distinto de 0 (incluso negativos).

El lenguaje C posee las siguientes estructuras de control de flujo:

- Secuenciacion: para ello usa el operador `;`, el cual es colocado al final de cada instrucción para indicar el fin de la misma, por lo tanto una instrucción se convierte en una instrucción formalmente en C cuando tiene el `;` al final. En otras palabras, es el terminador de instrucciones. Los `{}` son usados para agrupar declraciones e instrucciones en una instrucción compuesta, o _bloque_, de forma que su sintaxis sea equivalente a la de una instrucción sola. También, a C no le importan los saltos de línea. Es posible escribir un código en C en una sola línea y será completamente válido. Ejemplos:
    ```C
    #include <stdio.h>
    int main(void) {
        int x = 201; // ; al final de cada instruccion para separarla
        int a = 0; int b = 5; int c = a+b; // C no entiende los saltos de linea.
        printf("%d \n",c) // Imprime el valor de a + b = 5
        return 0; // ; al final de cada instruccion para separarla

    } 
    ```

- Seleccion: C posee los constructores de seleccion `if` y `switch`:
    - `if-else`: se usa para tomar decisiones, el `if` va seguido de paréntesis donde se indica la condición booleana a ser evaluada. `else` va sin paréntesis, y es opcional. Es posible escribir las instrucciones de cada `if-else` sin `{}` si es solo una instrucción, si es más de una requiere el uso de `{}`. Igual esto queda a criterio del programador.
    La condición booleana al final es ver si vale 0 o vale un número entero distinto a cero, tal como se mencionó al inicio. Ejemplo:
    ```C
    if (1)
    {
        printf("hola"); // En este ejemplo, else nunca se ejecutará ya que el if siempre es verdadero.
    }
    else
    {
        printf("chao");
    }
    ```
    - `else-if`: se usa para escribir en forma general cómo manejar múltiples decisiones, las cuales son evaluadas en el orden de aparición, si alguna es verdadera entonces es ejecutada su instrucción y no se vuelve a ejecutar el bloque de `else-if`. 
    ```C
    if (expresion)
    {
        instruccion
    }
    else if (expresion)
    {
        instruccion
    }
    else 
    {
        instruccion
    }
    ```
    El número de `else if` es arbitrario, y el uso de `else` es opcional.

    - `switch`: la instrucción `switch` también ofrece una forma de selección múltiple, que verifica si una expresión hace match a alguno de los valores constantes definidos en la instrucción, y ejecuta de acuerdo a ello. La sintaxis de `switch` es la siguiente:
    ```C
    swtich(c) {
        case '0': instruccion;
        case '1': instruccion;
        case '2': instruccion; break;
        case ' ': instruccion; break;
        default: instruccion; // Default viene siendo el caso cuando ninguna otra se ejecuta
        // sin embargo es opcional
    }
    ```
    En este caso, se compara la variable `c` con los valores después de cada `case`. Si alguno es igual, se ejecuta la instrucción. Cada valor debe ser diferente, además de constante. Luego, es necesario colocar un `break;` al final de cada instrucción para salir del switch, de lo contrario se seguirá ejecutando. En el caso anterior, si se entra al `case '0'` o `case '1'`, se seguirá el switch y se saldrá al entrar al `case '2'`, `case ' '` o `default`.
    - `?:` es una expresión condicional que permite reescribir un `if` en una sola línea. 
    ```C
    expresion1 ? expresion2 : expresion3
    ```
    Si `expresion1` es verdadero, se evalúa `expresion2` y es el valor retornado, de lo contrario se evalua `expresion3`. Sólo una de las dos expresiones 2 o 3 es evaluada.

- Repetición: en este caso se presentan `while`, `for` y `do while` de C:
    - `while`: esta instrucción evalúa una condición y ejecuta un bloque o instrucción de código mientras la condición sea verdadera. Para salir del "loop", se debe hacer falsa la condición o usar `break`. En este caso puede ser una repetición indeterminada.
    ```C
    while (condicion)
    {
        instruccion;
        instruccion;
    }
    ```
    - `do while`: es similar al while, sin embargo, se garantiza que habrá siempre una ejecución del bloque de código ya que la condición es evaluada después de ejecutarse el bloque de código. 
    ```C
    do {
        instruccion;
        instruccion;
    } while (condición)
    ```
    - `for`: la instrucción `for` viene siendo un azúcar sintáctico para un while de la forma
    ```C
    for (expresion1; expresion2; expresion3)
    {
        instruccion;
    }
    ```
    es equivalente a:
    ```C
    expresion1;
    while (expresion2)
    {
        instruccion;
        expresion3;
    }
    ```
    La idea del for es cuando se tiene alguna inicialización simple y un incremento, y es más visible.
    De esta forma, también es importante mencionar que en el caso `for (i = 0; i <n; i++)` por ejemplo, el valor de `i` se mantiene luego de la ejecución del `for`, y el valor de `n` puede ser alterado dentro del mismo bloque.

    Dado que un `for` es un `while`, entonces también sirve el uso de `break` para salir de la repetición.
    - `continue`: al igual que existe `break` para salir de loops como `while` y condicionales `switch`, con `continue` en vez de salir completamente del loop, se salta la iteración actual en los  `for`, `while` y `do while`, de forma que para el primero se ejecuta el incrimento y para `while`s se usa para volver a chequear la condición. Este no funciona en `switch`.
    - `goto`: a raíz de lo antiguo de C y la influencia de lenguajes como FORTRAN, existe el `goto` así como _etiquetas_ para usarse en conjunto con `goto`. Sin embargo, no es recomendable su uso y hasta es innecesario.

- Abstracción procedural: C permite definir subrutinas como procedimientos y funciones. El único detalle es que las funciones únicamente retornan un valor, sin embargo, es posible retoranar un `typedef` definido por el usuario y que el usuario lo adapte a sus necesidades. También, se puede usar el truco de usar apuntadores.

- Recursión: C también soporta la recursión de forma nativa.

- Concurrencia: el soporte de C para la concurrencia se logra con la librería `pthreads`, y es algo normal en el lenguaje. No recuerdo cómo se hace esto.

- Manejo de excepciones: C no posee un manejo nativo de excepciones como otros lenguajes. Sin embargo, es posible "manejar" errores gracias a la variable global `errno`, la cual tiene el valor numérico definido para el error. Luego se "maneja" usando ifs. No es igual a un `try catch` ya que no hay protección de código.

### 2
2. Diga en qué orden evalúan expresiones y funciones
El orden de evaluación de los operandos, expresiones y funciones es indeterminado. De hecho, puede quedar a decisión del compilador cambiar el orden para obtener una ejecución más eficiente.

Si bien en el caso de los operadores sí existe un orden de evaluación, que viene definido por la precedencia del operador, si se tiene el caso: `f(a)+f(b)*f(c)`, el orden de evaluación es `f(a)+(f(b)*f(c))` debido a la precedencia del operador `*`. Pero el cálculo del valor de `f(a)` podría hacerse antes de `f(b)` o `f(c)`, por ejemplo. 

Para el caso de las precedencias, se tiene:

|Operador | Asociatividad|
|----|----|
`() [] -> .` | izquierda a derecha |
`! ~ ++ -- + - * & (type) sizeof` | derecha a izquierda |
`* / % ` | izquierda a derecha |
`+ -` | izquierda a derecha |
`<< >>` (Bitwise shifts) | izquierda a derecha |
`< <= > =>`| izquierda a derecha |
`== !=`| izquierda a derecha |
`&` (Bitwise AND)| izquierda a derecha |
`^` (Bitwise XOR)| izquierda a derecha |
` \|` (Bitwise OR)| izquierda a derecha |
`&&` (AND)| izquierda a derecha |
`\|\|` (OR)| izquierda a derecha |
`?:`| derecha a izquierda |
` = += -= *= /= %= ^= &= \|= <<= >>= `| derecha a izquierda |
`,`| izquierda a derecha |
 
### 3
3. Diga qué tipos de datos posee y qué mecanismos ofrece para la creación de nuevos tipos (incluyendo tipos polimórficos de haberlos)

C posee pocos tipos de datos predefinidos.

| Nombre | Tamaño | Uso|
|---|---|---|
| `char` | Un byte | Un caracter|
|`int` | Depende del tamaño de entero de la maquina | Usado para enteros
|`float`| Número de punto flotante con precisión simple | Decimales sin tanta precisión
|`double`| Número de punto flotante con doble precisión | Números decimales de alta precisión

Es posible añadir un modificador como `short`, `long`, `signed` y `unsigned` a los números y también a los `char` de forma que se obtenga un tipo de dato "reducido" o más grande. Por ejemplo, en un procesador de 32 bits `short int` sería un entero de al menos 16 bits, mientras `int` podría ser de 16 o 32 bits. Para `long`, son de al menos 32 bits.

Para los chars, puede pasar que se diga `unsigned char` y aun cuando suene extraño, permite tener valores entre 0 y 255. Para un `signed char` se tendría entre -128 y 127. 

Para definir un "string" se usa un arreglo de `char`.

C permite definir nuevos "tipos" de datos, usando lo que son las estructuras, `typedef` y `unions`.

##### Estructuras
- Las estructuras agrupan otros tipos de datos. Se definen con `struct`, por ejemplo:
```C
struct fecha {
    int dia;
    int mes;
    int anno;
}

int main()
{
    struct fecha hoy = {13,11,2023}; // Aqui se declara un struct tipo fecha llamado "hoy"
    return 0;
}
```
Luego, para "obtener" valores de un `struct` se usa el operador `.`, por ejemplo: `hoy.dia` retornaria `11`.

##### typedef

`typedef` no define un tipo de datos nuevo, si no que permite definir un alias para un tipo de datos existente, de forma que no sea necesario escribir en la declaración `struct nombre_struct nombre_variable`. Ejemplo siguiendo la definición del `struct fecha`
```C
typedef struct fecha date;
...
int main()
{
    date hoy = {13,11,2023};
    return 0;
}
```

De esa forma se usó `date` como un alias para el `struct fecha`

##### Uniones

Son similares a los `struct`s, ya que agrupa varios elementos de diferentes tipos, sin embargo, el espacio reservado en memoria es el mayor de todos lso elementos, y por lo tanto todos comparten el mismo espacio de memoria reservado, de forma que solo uno de los elementos puede existir en un Union.

```C
union nums
{
    int num;
    float num2;
}
```

En este caso, el tamaño reservado del union `nums` es del tamaño del float en memoria. Si se asigna un valor a `num` y luego a `num2`, sobreescribirá en memoria estos valores.

C no tiene soporte para polimorfismo de forma nativa.

##### Enums

Es un tipo de datos definido por el usuario, con la intención de definir constantes para una variable única de enumeración. Se definen:

```C
enum vocales {a,e,i,o,u};
```

Con esto se definió el `enum` llamado `vocales`. Para instanciar una variable se hace:
```C
enum vocales {a,e,i,o,u};
enum vocales voc;
voc = a;
```

La idea de esto, es que al asignarle `voc = a`,  el valor asociado a la variable `voc` va a ser 0, ya que los `enum` enumeran sus elementos desde el 0, por lo tanto, $a = 0, e = 1, i = 2, o = 3, u = 4$.

Es posible también establecer los valores iniciales para los enum, por ejemplo:
```C
enum vocales {a=1,e,i,o,u};
```
En este caso empezamos a contar desde el 1 en vez del 0.

### 4

- C es estáticamente tipado. Todas las variables deben declararse con su tipo de datos, además que se chequea a tiempo de compilación.
- C usa equivalencia estructural para todos los tipos excepto para los structs, donde usa equivalencia de nombres. De forma que para operar dos variables, verifica los tipos para evitar por ejemplo sumar un char con un int.
- C no posee inferencia de tipos.
- C permite convertir tipos usando el casting, pero esto solo se puede para tipos explícitos.
- C realiza cierta coerción de tipos para los números, donde permite realizar una operaciones entre un int y un float. También se puede realizar reasignaciones a variables de diferentes tipos, pero esto puede afectar al tipo de acuerdo a la conversión necesaria.
- C posee el tipo `void*` para definir un tipo de referencia universal.