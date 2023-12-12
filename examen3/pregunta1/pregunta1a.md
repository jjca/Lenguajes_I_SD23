# Pregunta 1a

1. Explique la manera de crear y manipular objetos que tiene el lenguaje, incluyendo: constructores, métodos, campos, etc. 

Kotlin implementa los constructores directamente en la definición de la clase. Todo objeto tiene su constructor primario, sin embargo es posible añadir nuevos constructores adicionales.

Un objeto se crea con un constructor:

```kotlin
class Persona(val nombre:String, val apellido: String){
    // metodos
}
```

```kotlin
class Persona(val nombre:String, val apellido: String){
    val variable1: Tipo
    fun nombreApellido() : String{
        println("La persona se llama:"nombre+" "+apellido)
    }
}
```

Los parámetros pueden incluir también el valor predeterminado directamente en el constructor, por ejemplo colocando: `val nombre: String = Jorge`

Es posible además tener constructores secundarios, los cuales se definen dentro de la clase con la expresión `constructor`:

```kotlin
class Persona(val nombre:String, val apellido:String){
    val hijos: MutableList<Persona> = mutableListOf()
    constructor(nombre: String, apellido: String, padre: Person) : this(nombre, apellido){
        padre.hijos.add(this)
    }
}
```

Es necesario delegar al constrcutor principal la creación del objeto de forma directa o indirecta. Esto se hace usando `this()`.

Los objetos son finales, y su asociación es estática. No es posible sobrecargar los métodos ni sus propiedades.

Una clase puede admitir sobrecargas en clases que lo heredan, la superclase debe tener `open` en su declaración. Los métodos y propiedades deben llevar `open` tambièn.

La visibilidad de los objetos, parámetros y métodos en Kotlin puede ser:

- public: accesible en cualquier lado
- private: solo accesible desde el alcance actual
- protected: solo accesible de la clase actual, y de sus subclases
- internal: solo en el módulo actual

Kotlin además tiene clases abstractas e interfaces. Las abstractas pueden ser consideradas como plantillas, y son abiertas por defecto. Las interfaces permiten definir funciones pero no tienen estados.

Los campos en un objeto tienen su nombre, tipo, así como si es `val` o `var`. 

Además de los tipos "clásicos" están los tipos `data`, `enum`.

Los `data` permiten almacenar datos y el compilador automáticamente declara las siguientes funciones: `equals()/.hashCode()`, `.toString()` de la forma: `"User(name=John, age=42)"`, `.componentN()` y `copy()`.

Los `enum` son como los `enum` de C:

2. Describa el funcionamiento del manejo de memoria, ya sea explícito (new/delete) o implícito (recolector de basura).

Usa un manejador de memoria simiar al de JVM y cuenta con un recolector de basura. Los objetos se almacenan en un heap compartido y se les puede acceder por cualquier hilo del programa. El recolector realiza una limpieza con frecuencia para ubicar objetos no alcanzables.

Kotlin también tiene su propio asingador de memoria, el cual divide la memoria en páginas lo cual permite intercambios independientes. Cda asignación se convierte en un bloque dentro de una página. El propio asignador tiene protecciones para picos de asignación de memoria, permite verificar memory leaks y ajustar el consumo de memoria.

Es posible desactivar el recolector de basura de forma manual.

3. Diga si el lenguaje usa asociación estática o dinámica de métodos y si hay forma de alterar la elección por defecto del lenguaje.

El lenguaje posee asociación estática de métodos de forma predeterminada pero es posible usar la asignación dinámica.

Es necesario usar la palabra clave `override` dentro del método a ser sobreescrito, además de que se necesita que el método tenga `open` en la superclase para usar asociaión dinámica.

4. Describa la jerarquía de tipos, incluyendo mecanismos de herencia múltiple (de haberlos), polimorfismo paramétrico (de tenerlo) y manejo de varianzas.

La jerarquía de tipos de Kotlin tiene su raíz en el tipo `Any`, tal como el tipo `Object` de Java. Además, todos los tipos tienen el subtipo `Nothing`, que es el fondo, no existen subtipos de `Nothing`.

Todos los tipos de Kotlin maneja el caso de ser nulos, donde se tiene el "?" al final del tipo, es decir, `Any?`, `Nothing?`. Esto ofrece Null safety, ya que si un parámetro no tiene ? y recibe el Null, entonces la ejecución se detiene. Para el caso donde sí sea posible, es necesario el ?.

El tipo `Unit` es un tipo especial para cuando una función no se le especifica un tipo de retorno

Kotlin también posee los tipos Byte, Short, Int, Long para números enteros. Float y Double para punto flotante. Está el caso Unsigned equivalente, UByte, UShort, UInt y ULong. Los caracteres se representan con Char, Strings con String y pueden declararse de una sola linea y multilinea.

Finalmente, la clase Array para los arreglos de tamaño fijo

No hay herencia múltiple de clases, pero sí aplica para interfaces.

Kotlin tiene polimorfismo general, y a tiempo de compilación. Es posible sobreescribir métodos de clases que hayan sido definidos en alguna superclase, pero se requiere que sean definidos con `open`.

Kotlin no tiene los mismos genéricos de Java tipo "wildcard", en este caso se tiene declaración de varianza en sitio.

El manejo de la covarianza se realiza usando el modificador `out`, donde se asegura que el valor del tipo `T` será de solo lectura. Por ejemplo, la interfaz `List` en Kotlin es así.

Para manejar la contravarianza, se usa el modificador `in` al valor `T`en la declaración de la clase., lo cual asegura que será manejado en la clase. Así mismo se necesita que sea privado el manejador que cambie los valores de este elemento.