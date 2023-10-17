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
    
    def addProgram(self,program,quantity):
        if self.free_memory < quantity:
            raise memoryNoAvailable
        
        if self.searchFreeMemory(self.root,program,quantity):
            self.programs.append(program)

    def searchProgram(self,program_name):
        for prog in self.programs:
            if prog.name == program_name:
                print("program exists")
                return True
        return False
    
    def addNodes(self,node_i,node_d):
        self.nodes.append(node_i)
        self.nodes.append(node_d)

    def searchFreeMemory(self,node,program,quantity):
        level = math.ceil(math.log2(quantity))
        print(f"buscando memoria en el nodo {node}")
        print(f"nivel requerido: {level}")
        if node.program == None and node.level == level:
            print("Estamos en un nodo con capacidad")
            node.reserveNode(program)
            self.free_memory = self.total_size - 2**level
            print(f"quedan: {self.free_memory}")
            return True
        else:
            print("dando a luz")
            self.searchFreeMemory(node.giveBirth()[0],program,quantity)
       
    
"""
class MemorySector:
    def __init__(self,memory_size):
        self.sector_size = memory_size
        self.sector_range = [range]

    def __str__(self):
        return self.sector_size

    def __repr__(self):
        return f'{self.sector_size}' """
    

class Node:
    def __init__(self,pure,start,end,id,level):
        self.pure = pure
        self.bendicion_i = None
        self.bendicion_d = None
        self.start = start
        self.end = end
        self.id = id
        self.program = None
        self.level = int(level)

    def reserveNode(self,program):
        self.program = program

    def giveBirth(self):
        self.bendicion_i = Node(self.id,math.ceil(self.start/2),math.floor((self.end/2)),self.id+1,self.level-1)
        self.bendicion_d = Node(self.id,self.bendicion_i.end+1,self.end,self.id+1,self.level-1)
        #print(self.bendicion_i)
        #print(self.bendicion_d)
        #print("Alo")
        #print(self)
        return self.bendicion_i,self.bendicion_d

    def __repr__(self):
        return f'\n### papa: {self.pure}, rango {self.start},{self.end}, nivel {self.level}, programa: {self.program} \n \t hijo izq {self.bendicion_i}, \t hijo der: {self.bendicion_d}'

class Program:
    def __init__(self,name):
        self.name = name

def main():
    print("Hola")
    correct = 0
    while not correct:
        try:
            memory_size = int(input("Introduzca la cantidad de bloques. Use potencias de dos y numeros positivos\n"))
        except ValueError:
            print("El valor no es un número")
            continue
        if memory_size > 0 and memory_size < 1024000 :
            log = math.log2(memory_size)
            if math.ceil(log) == math.floor(log):
                print("Potencia de dos")
                correct = 1
            else:
                print("ERROR: Por favor introduzca una potencia de 2")
        else:
            print("ERROR: Por favor introduzca un número positivo")
    root = Node(None,0,memory_size-1,0,math.log2(memory_size))
    memory = Memory(memory_size,root)
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

    #Memoria = Memory()

if __name__ == "__main__":
    main()