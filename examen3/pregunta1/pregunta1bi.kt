abstract class Secuencia<T> {
    val elems = mutableListOf<T>()
    abstract fun agregar(elem: T) : Boolean // Recibe un elemento y lo agrega a la secuecnia
    abstract fun remover() : T? // Devulve el elemento a ser removido y lo elimina. Da error si ta vacia
    abstract fun vacio() : Boolean // Dice si la secuencia esta vacia
}

class Cola<T>() : Secuencia<T>() {
    override fun agregar(elem: T) : Boolean {
        return elems.add(elem)
    }
    override fun remover() : T? {
        try {
            return elems.removeFirst()
        } catch (e: NoSuchElementException)
        {
            println("Cola vacia")
            return null
        }    
    }

    override fun vacio() : Boolean {
        return elems.isEmpty()
    }
    
    fun listar() : String {
        return elems.joinToString()
    }

    fun quitar() : T? {
        return elems.firstOrNull()
    }
}

class Pila<T>() : Secuencia<T>() {
    override fun agregar(elem: T) : Boolean {
        return elems.add(elem)
    }
    override fun remover() : T? {
        try {
            return elems.removeLast()
        } catch (e: NoSuchElementException)
        {
            println("Pila vacia")
            return null
        }
    }

    override fun vacio() : Boolean {
        return elems.isEmpty()
    }
    
    fun listar() : String {
        return elems.joinToString()
    }
}

fun main() {
    val colita = Cola<Int>()
    colita.agregar(1)
    println(colita.listar())
    colita.agregar(4)
    colita.agregar(6)
    println(colita.listar())
    println("Quitmos el 1")
    println(colita.remover())
    println(colita.remover())
    println(colita.remover())
    println(colita.remover())
    println(colita.listar())
    
    val pilita = Pila<Int>()
    pilita.agregar(2)
    pilita.agregar(7)
    pilita.agregar(9)
    println(pilita.listar())
    println("Quitando el 9")
    println(pilita.remover())
    println(pilita.remover())
    println(pilita.remover())
    println(pilita.remover())
    println(pilita.listar())

}