import sys
import math

class memoryNoAvailable(Exception):
    "La capacidad es menor a la requerida"
    pass

class Memory:
    def __init__(self,memory_size,root):
        self.total_size = int(memory_size)
        self.free_memory = self.total_size
        self.root = root
        self.programs = []
        self.nodes = []
    
    def addProgram(self,program_name,quantity):
        if self.free_memory < quantity:
            raise memoryNoAvailable
        
        if self.searchFreeMemory(self.root,program_name,quantity):
            program = Program(program_name,quantity)
            self.programs.append(program)
        else:
            print("No se guardo??")
            return False

    def searchProgram(self,program_name):
        for prog in self.programs:
            if prog.name == program_name:
                print("program exists")
                return True
        return False
    
    def addNode(self,node):
        self.nodes.append(node)

    """
    Función que ubica los nodos libres y realiza la reservación
    Un nodo "reservado" no siempre tiene un programa, es que al menos uno de 
    sus hijos tiene un programa almacenado y está reservado.
    """
    def searchFreeMemory(self,node,program,quantity):
        # El nivel viene determinado por el logaritmo 2 de la cantidad de memoria a ser
        # reservada. 
        level = math.ceil(math.log2(quantity))
        # Variable para mantener lo retornado
        return_value = False
        print(f"buscando memoria en el nodo {node.id}")
        print(f"nivel requerido: {level}")
        print(f"nivel actual: {node.level}")
        if node.level != level:
            # Si el nodo no está reservado
            if not node.reserved and node.program == None:
                # Si no tiene hijos 
                if node.bendicion_i == None:
                    # Creamos los hijos
                    bendicion_i, bendicion_d = node.giveBirth(len(self.nodes))
                    self.addNode(bendicion_i)
                    self.addNode(bendicion_d)

                # Recorremos el arbol por la izquierda
                return_value = self.searchFreeMemory(node.bendicion_i,program,quantity)

                # Si nos dicen que no hay espacio en el lado izquierdo, a por el derecho
                if not return_value:
                    return_value = self.searchFreeMemory(node.bendicion_d,program,quantity)

                return return_value
            
            else:
                return False
                
        else: 
            # Estoy en el nivel que es y veo que no tenga hijos, ya que
            # si tiene entonces no puedo reservar
            print(f"node: {node.id}")
            if node.bendicion_i == None and node.program == None and not node.reserved:
                node.addProgram(program)
                print("Reservado")
                return True
            
            else:
                # En este caso hay hijos, no se puede reservar
                return False
    
    """
    Quitamos las bendiciones (hijos) de los nodos al liberar memoria
    """
    def quitarBendiciones(self,node):
        del node.bendicion_i
        del node.bendicion_d
        node.bendicion_i = None
        node.bendicion_d = None

        # Eliminamos los nodos de la lista

        for node_bendicion in self.nodes:
            if node_bendicion.pure_id == node.id:
                self.nodes.remove(node_bendicion)


    """
    Función para liberación de memoria. Esto se hace recorriendo el arbol
    recursivamente y se ubica el programa, al hacerlo se elimina dicho
    programa y luego se liberan los hijos
    """
    def freeMemory(self,node,program):

        return_val_i = False
        return_val_d = False

        if node.program == None:
            if node.bendicion_i != None:
                return_val_i = self.freeMemory(node.bendicion_i,program)
                return_val_d = self.freeMemory(node.bendicion_d,program)

                if return_val_i and return_val_d:
                    self.quitarBendiciones(node)
                    print("Se eliminaron los hijos")
                    return True
                
                return False
            return True
        
        else:
            if node.program == program:
                node.program = None
                node.reserved = False
                for prog in self.programs:
                    if prog.name == program:
                        self.programs.remove(prog)
                return True
            else:
                return False
class Node:
    def __init__(self,pure,start,end,id,level):
        self.pure = pure
        if self.pure == None:
            self.pure_id = -1
        else:
            self.pure_id = self.pure.id
        self.bendicion_i = None
        self.bendicion_d = None
        self.start = start
        self.end = end
        self.id = id
        self.program = None
        self.level = level
        self.reserved = False

    def addProgram(self,program):
        self.program = program
        if self.pure == None:
            pass
        self.reserved = True

    def reserveNode(self):
        self.pure.reserved = True
        self.reserved = True

    def giveBirth(self,curr_id):
        self.bendicion_i = Node(self,math.ceil(self.start/2),math.floor((self.end/2)),curr_id,self.level-1)
        self.bendicion_d = Node(self,self.bendicion_i.end+1,self.end,self.bendicion_i.id+1,self.level-1)
        return self.bendicion_i,self.bendicion_d

    def __str__(self):
        return f'\n### papa: {self.pure_id}, id: {self.id} rango {self.start},{self.end}, nivel {self.level}, programa: {self.program} reservado {self.reserved} \n \t hijo izq {self.bendicion_i}, \t hijo der: {self.bendicion_d}' 

class Program:
    def __init__(self,name,quantity):
        self.name = name
        self.memory = quantity

    def __str__(self):
        return f"programa: {self.name}, memoria: {self.memory}"

def main():
    print("Hola")
    correct = 0
    while not correct:
        try:
            memory_size = int(input("Introduzca la cantidad de bloques. Use potencias de dos y numeros positivos\n"))
        except ValueError:
            print("El valor no es un número")
            continue
        if 0 < memory_size < 1024000:
            log = math.log2(memory_size)
            if math.ceil(log) == math.floor(log):
                print("Potencia de dos")
                correct = 1
            else:
                print("ERROR: Por favor introduzca una potencia de 2")
        else:
            print("ERROR: Por favor introduzca un número positivo")
    root = Node(None,0,memory_size-1,0,int(math.log2(memory_size)))
    memory = Memory(memory_size,root)
    memory.addNode(root)
    #print(root)
    for line in sys.stdin:
        print("De algo")
        entrada = line.rstrip().split(" ")
        if 'salir' == line.rstrip().lower():
            break
        elif 'reservar' == entrada[0].lower() and len(entrada) == 3:
            try:
                quantity = int(entrada[1])
                try: 
                    if quantity > memory.total_size:
                        print("Memoria no disponible")
                except:
                    raise memoryNoAvailable
                if (not memory.searchProgram(entrada[2].lower())):
                    memory.addProgram(entrada[2].lower(),quantity)
                else:
                    print("programa existe")
                    continue
            except ValueError:
                print("La cantidad no es numero, intente nuevamente")
                continue
        elif 'tree' == entrada[0]:
            print(root)
        elif 'prog' == entrada[0]:
            for prog in memory.programs:
                print(f"#### {prog}")

    #Memoria = Memory()

if __name__ == "__main__":
    main()