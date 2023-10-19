import sys
import math

class memoryNoAvailable(Exception):
    "La capacidad es menor a la requerida"
    pass

class inputError(Exception):
    "Error de entrada"
    pass
class programDoesNotExists(Exception):
    "No existe el programa"
    pass

class programDoesExists(Exception):
    "No existe el programa"
    pass

"""
Clase memoria para manejo de los objetos y listas
"""
class Memory:
    def __init__(self,memory_size,root):
        self.total_size = int(memory_size)
        self.free_memory = self.total_size
        self.root = root
        self.programs = []
        self.nodes = []
    
    def addProgram(self,program_name,original_name,quantity):
        if self.free_memory < quantity:
            raise memoryNoAvailable
        
        if self.searchFreeMemory(self.root,program_name,original_name,quantity):
            program = Program(program_name,quantity)
            self.programs.append(program)
        else:
            return False

    def searchProgram(self,program_name):
        for prog in self.programs:
            if prog.name == program_name:
                return True
        return False
    
    def addNode(self,node):
        self.nodes.append(node)

    """
    Función que ubica los nodos libres y realiza la reservación
    Un nodo "reservado" no siempre tiene un programa, es que al menos uno de 
    sus hijos tiene un programa almacenado y está reservado.
    """
    def searchFreeMemory(self,node,program,original_name,quantity):
        # El nivel viene determinado por el logaritmo 2 de la cantidad de memoria a ser
        # reservada. 
        level = math.ceil(math.log2(quantity))
        # Variable para mantener lo retornado
        return_value = False
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
                return_value = self.searchFreeMemory(node.bendicion_i,program,original_name,quantity)

                # Si nos dicen que no hay espacio en el lado izquierdo, a por el derecho
                if not return_value:
                    return_value = self.searchFreeMemory(node.bendicion_d,program,original_name,quantity)

                return return_value
            
            else:
                return False
                
        else: 
            # Estoy en el nivel que es y veo que no tenga hijos, ya que
            # si tiene entonces no puedo reservar
            if node.bendicion_i == None and node.program == None and not node.reserved:
                node.addProgram(program,original_name,quantity)
                self.free_memory = self.free_memory - 2**level
                return True
            
            else:
                # En este caso hay hijos, no se puede reservar
                return False
    
    """
    Quitamos las bendiciones (hijos) de los nodos al liberar memoria
    """
    def quitarBendiciones(self,node):

        pure_id = node.id
        # Eliminamos los nodos de la lista
        node.bendicion_i = None
        node.bendicion_d = None
        newlist = []
        for nodes in self.nodes:
            if nodes.pure_id != pure_id:
                newlist.append(nodes)
        self.nodes = newlist
        

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
                    return True
                
                return False
            return True
        
        else:
            if node.program == program:
                node.program = None
                node.reserved = False
                node.memory = 0
                for prog in self.programs:
                    if prog.name == program:
                        self.programs.remove(prog)
                return True
            else:
                return False

"""
Clase nodo que define los parámetros y métodos de los nodos
"""
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
        self.program_original_name = None
        self.level = level
        self.reserved = False
        self.memory = 0
    """
    Agrega el programa al objeto nodo y lo marca como reservado
    """
    def addProgram(self,program,original_name,memory):
        self.memory = memory
        self.program = program
        self.program_original_name = original_name
        if self.pure == None:
            pass
        self.reserved = True

    """
    Crea (da a luz) a los hijos del nodo pure (padre)
    """
    def giveBirth(self,curr_id):
        self.bendicion_i = Node(self,math.ceil(self.start/2),math.floor((self.end/2)),curr_id,self.level-1)
        self.bendicion_d = Node(self,self.bendicion_i.end+1,self.end,self.bendicion_i.id+1,self.level-1)
        return self.bendicion_i,self.bendicion_d

    """
    Representación del árbol de memoria
    """
    def __str__(self):
        return f'\n### papa: {self.pure_id}, id: {self.id} rango {self.start},{self.end}, nivel {self.level}, programa: {self.program} reservado {self.reserved} \n \t hijo izq {self.bendicion_i}, \t hijo der: {self.bendicion_d}' 

class Program:
    def __init__(self,name,quantity):
        self.name = name
        self.memory = quantity

    def __str__(self):
        return f"programa: {self.name}, memoria: {self.memory}"

def main():
    correct = 0
    while not correct:
        try:
            memory_size = int(input("Introduzca la cantidad de bloques. Use potencias de dos y números positivos\n"))
            if 0 < memory_size < 1024000:
                log = math.log2(memory_size)
                if math.ceil(log) == math.floor(log):
                    correct = 1
                else:
                    print("ERROR: Por favor introduzca una potencia de 2")
            else:
                print("ERROR: Por favor introduzca un número positivo")

        except ValueError:
            print("El valor no es un número")
            continue
    root = Node(None,0,memory_size-1,0,int(math.log2(memory_size)))
    memory = Memory(memory_size,root)
    memory.addNode(root)
    activo = True
    while activo:
        entrada = list(input("Introduzca una opción válida. Para más información escriba HELP:  ").split())
        if 'salir' == entrada[0].lower() and len(entrada) == 1:
            activo = False
            break
        elif 'reservar' == entrada[0].lower() and len(entrada) == 3:
            try:
                quantity = int(entrada[1])
                try: 
                    if quantity > memory.total_size:
                        raise memoryNoAvailable
                    if len(entrada[2].lower()) == 0 or len(entrada) < 3:
                        print("Nombre del programa vacio")
                        raise inputError
                    if (not memory.searchProgram(entrada[2].lower())):
                        memory.addProgram(entrada[2].lower(),entrada[2],quantity)
                        print (f"Memoria reservada para el programa {entrada[2]}")
                    else:
                        raise programDoesExists
                except memoryNoAvailable:
                    print("Memoria no disponible para reservar")
                    continue
                except inputError:
                    print("Por favor introduzca los datos correctamente")
                    continue
                except programDoesExists:
                    print("El programa ya existe No puede reservarse memoria")
                    continue
            except ValueError:
                print("La cantidad no es numero, intente nuevamente")
                continue
        elif 'liberar' == entrada[0].lower() and len(entrada) == 2:
            try:
                if (memory.searchProgram(entrada[1].lower())):
                    memory.freeMemory(memory.root,entrada[1].lower())
                    print(f"Memoria del programa {entrada[1]} liberada")
                else:
                    raise programDoesNotExists
            except programDoesNotExists:
                print("El programa indicado no existe. No se puede liberar memoria no reservada")
                continue
        elif 'mostrar' == entrada[0].lower():
            print("Memoria en uso:")
    
            for node in memory.nodes:
                if node.memory > 0:
                    print(f"\t Programa: {node.program_original_name} - Memoria en uso: {node.memory} - Bloque en uso: {2**node.level}")
            print("Memoria libre")
            free = []
            for node in memory.nodes:
                if (node.memory == 0 and node.bendicion_i == None):
                    free.append(2**node.level)
            print(f"\t Hay libres: {free} bloques", end =" \n")
    
        elif 'prog' == entrada[0].lower() and len(entrada) == 1:
            for prog in memory.programs:
                print(f"#### {prog}")
        elif 'help' == entrada[0].lower() and len(entrada) == 1:
            print("\n Los siguientes comandos están disponibles:")
            print("RESERVAR <cantidad> <nombre>: Debe indicar la cantidad de memoria a reservar (número entero) y el nombre del programa a reservarle su memoria")
            print("LIBERAR <nombre>: Debe indicar el nombre del programa a liberarle su memoria")
            print("MOSTRAR: Muestra el estado de la memoria")
            print("HELP: muestra este mensaje")
            print("SALIR: sale del programa")
            print("PROG: muestra la lista de programas almacenados\n")

if __name__ == "__main__":
    main()