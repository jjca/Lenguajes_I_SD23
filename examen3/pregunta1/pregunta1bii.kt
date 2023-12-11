class ElementoYaExiste(message: String) : Exception(message)

class nullNode(message: String) : Exception(message)

abstract class Busqueda {
    abstract fun buscar(G:Grafo, D: Int, H: Int) : Int 
}

data class Vertice<Int>(val indice: Int, val valor: Int)

data class Lado(val a: Vertice<Int>, val b: Vertice<Int>)

class Grafo(){
    val listaAdyacencias = mutableMapOf<Vertice<Int>, ArrayList<Vertice<Int>>>()

    fun crearVertice(v: Int) : Vertice<Int> {
        val vertice = Vertice(listaAdyacencias.count(),v)
        listaAdyacencias.keys.forEach{
            if (it.valor == v){
                throw ElementoYaExiste("El vertice ya existe")
            }
        }
        if (listaAdyacencias.contains(vertice))
        {
            throw ElementoYaExiste("El vertice ya existe")
        }
        listaAdyacencias[vertice] = arrayListOf()
        return vertice
    }

    fun crearLado(a: Vertice<Int>, b: Vertice<Int>) : Vertice<Int> {
        listaAdyacencias[a]?.add(b)
        return b
    }
    
    override fun toString() : String {
        return buildString { listaAdyacencias.forEach { (vertice, vertAdy) ->
            val lado = vertAdy.joinToString { it.valor.toString() }
            append("${vertice.valor} -> [$lado]\n")}}
    }
}

class DFS() : Busqueda() {
    override fun buscar(G: Grafo, D: Int, H:Int) : Int {
        val largo = G.listaAdyacencias.keys.size
        val visitados = BooleanArray(largo){false}
  //      println(visitados.joinToString())
        val pila = ArrayDeque<Int>()
        pila.add(D)
    //        println(pila)
        while (pila.size > 0){
            val elem = pila.removeLast()
            if (!visitados.get(elem)){
               // println("No visitado")
                visitados.set(elem,true)
            }
            //println(visitados.joinToString())
            if (visitados.get(H))
            {
                break
            }
            val adyacentes = G.listaAdyacencias.filterKeys{it.valor == elem}
            //println("alo")
            //println(adyacentes)
            adyacentes.values.forEach{
                it.forEach{
                    if (!visitados.get(it.valor)){
                        pila.add(it.valor)
                    }
                }
            }
            if (pila.contains(H)){
                visitados.set(H,true)
                break
            }
        }
        if (visitados.get(H))
        {
          //  println(visitados.joinToString())
            return visitados.fold(0){acc, e -> if (e) acc+1 else acc}
        }
        else {
        //    println(visitados.joinToString())
            return -1
        }
    }
} 

class BFS() : Busqueda() {
    override fun buscar(G: Grafo, D: Int, H:Int) : Int {
        val largo = G.listaAdyacencias.keys.size
        val visitados = BooleanArray(largo){false}
        //println(visitados.joinToString())
        val cola = ArrayDeque<Int>()
        cola.add(D)
//        println(pila)
        visitados.set(D,true)
        while (cola.size > 0){
            val elem = cola.removeFirst()
            /* if (!visitados.get(elem)){
               // println("No visitado")
                visitados.set(elem,true)
            } */
            //println(visitados.joinToString())
            if (visitados.get(H))
            {
                break
            }
            val adyacentes = G.listaAdyacencias.filterKeys{it.valor == elem}
            //println("alo")
          //  println(adyacentes)
            adyacentes.values.forEach{
                it.forEach{
                    if (!visitados.get(it.valor)){
                        visitados.set(it.valor,true)
                        cola.add(it.valor)
                    }
                }
            }
            if (cola.contains(H)){
                visitados.set(H,true)
                break
            }
        }
        if (visitados.get(H))
        {
            //println(visitados.joinToString())
            return visitados.fold(0){acc, e -> if (e) acc+1 else acc}
        }
        else {
            //println(visitados.joinToString())
            return -1
        }
    }
} 

fun main() {
    val grafo1 = Grafo()
    val vertice0 = grafo1.crearVertice(0)
    val vertice1 = grafo1.crearVertice(1)
    val vertice2 = grafo1.crearVertice(2)
    val vertice3 = grafo1.crearVertice(3)
    val vertice4 = grafo1.crearVertice(4)
    val vertice5 = grafo1.crearVertice(5)
    grafo1.crearLado(vertice0,vertice1)
    grafo1.crearLado(vertice1,vertice2)
    grafo1.crearLado(vertice3,vertice4)
    grafo1.crearLado(vertice1,vertice3)
    grafo1.crearLado(vertice0,vertice5)
    println(grafo1)
    println(grafo1.listaAdyacencias)
    // Caso donde falla
    println(DFS().buscar(grafo1,1,0))
    // Caso con exito
    println(DFS().buscar(grafo1,1,4))

    println(BFS().buscar(grafo1,1,4))





}