# Pregunta 1a)
## Jorge Correia - 14-12054

Para responder esta pregunta se usó el lenguaje de programación Java. Su elección además de seguir con el enunciado de la pregunta, es un lenguaje de programación con trayectoria y estabilidad.

- De una breve descripción del lenguaje escogido.
    1. Diga qué tipo de alcances y asociaciones posee, argumentando las ventajas y desventajas de la decisión tomada por los diseñadores del lenguaje, en el contexto de sus usuarios objetivos.
    2. Diga qué tipo de módulos ofrece (de tenerlos) y las diferentes formas de importar y exportar nombres.
    3. Diga si el lenguaje ofrece la posibilidad de crear aliases, sobrecarga y polimorfismo. En caso afirmativo, dé algunos ejemplos. 
    4. Diga qué herramientas ofrece a potenciales desarrolladores, como: compiladores, intérpretes, debuggers, profilers, frameworks, etc.

## Respuestas

### 1

El alcance que posee Java es estático y dinámico. Ocurre cuando se tiene una clase que redefine un método heredado en otra clase. La asociación es profunda.

Java fue desarrollado para ofrecer un software para una amplia variedad de dispositivos, y que fuera pequeño, portatil y distribuido. Es por ello que Java es tan flexible en su ejecución sin que dependa del sistema operativo, únicamente se necesita la JVM para poder ejecutar todo código de Java.

El hecho de tener alcance estático permite entender el código sin necesidad de ejecutarlo, así como también el dinámico para permitir el uso de diferentes métodos con el mismo nombre de acuerdo al caso.

### 2
Java posee los llamados _packages_, que vendrían siendo equivalentes a los módulos. Estos son colecciones de clases e interfaces relacionadas, permitiendo tener privilegios de acceso y gestión del esapcio de nombres. De esta forma se pueden agrupar fácilmente. 

Java posee _packages_ que vienen predefinidos y vienen en el JDK. También están los paquetes definidos por el usuario. 

Para importar un paquete se puede usar las siguientes opciones:

```
import java.lang.*;
import java.lang.String;
```

El primer caso importa todas las clases dentro del _package_ `java.lang`, mientras que el segundo importa es la clase `java.lang.String` únicamente.

Simplemente para usarlo se requiere ahora usar `String`

Para los permisos de exportación de un _package_, se determinan usando las palabras reservadas _public, private, protected_ y la misma que se usa para definir un _package_, la palabra _package_ que determinan los permisos correspondientes de acuerdo al caso.

Java no puede manejar los casos cuando existe colisión de nombres entre dos clases de diferentes _packages_. Es necesario usar el nombre completo de la clase en el _package_ para poderlo usar.

### 3

Java ofrece la posibilidad de usar **alias**. Por ejemplo, suponiendo exista la clase Alias

```
Alias a1 = new Alias(args);
Alias a2 = a1;
```

`a2` haría referencia a `a1`.

Java ofrece **sobrecarga** por ejemplo con el operador `+`, permitiendo concatenar cadenas y también sirve para realizar sumas de enteros o de flotantes.

```
String parte1 = "Hola";
String parte2 = "mundo";

String completa = parte1+parte2;

System.out.println(completa)
```
La string `completa` retorna `Hola mundo`

También está el caso de `++` el cual permite realizar un postincremento o preincremento de acuerdo al caso si es prefijo o postfijo.

```
int a = 2;
System.out.println(a++);
System.out.println(++a);
```

Para el `a++`, primero se retorna su valor y luego se le incrementa en 1. Por ello, el primer print imprime 2.

Para `++a`, primero se incrementa en 1 y luego se retorna el valor. El segundo print, imprimiría 4, ya que la primera instrucción hizo que `a` fuera 3 y luego 4.

Finalmente, el **polimorfismo**. Java soporta polimorfismo a través de los genéricos, los cuales ofrecen la posibilidad a un método de aceptar diferentes tipos de datos, sin realizar una sobrecarga del mismo.

### 4

Para Java se tienen los IDE Eclipse, IntelliJ IDEA y NetBeans para trabajar, sin embargo, no es necesario ya que puede ser codeado sin problemas sin estos. 

Para compilar es necesario tener el Java Development Kit, este está disponible tanto en el sitio web de Oracle como lo es el OpenJDK, se tiene el compilador javac.

El interprete de Java viene incluido en el Java Runtime Environment, el que permite ejecutar el comando `java` para ejecutar el código en la Java Virtual Machine

Por el lado de los frameworks se encuentra Spring, Spring Boot, Struts, Apache Wicket.

Un debugger puede ser el Java Discovery Protocol, que lo provee directamente Oracle. Así mismo, los que vienen incluidos directametne en los IDE como IntelliJ y Eclipse.
Diga qué herramientas ofrece a potenciales desarrolladores, como: compiladores, intérpretes, debuggers, profilers, frameworks, etc.

Profilers, se tienen JProfiler, Netbeans Profiler, IntelliJ Profiler, etc.