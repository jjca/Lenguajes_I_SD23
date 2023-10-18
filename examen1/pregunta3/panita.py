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

    def searchFreeMemory(self,node,program,quantity):
        level = math.ceil(math.log2(quantity))
        print(f"buscando memoria en el nodo {node.id}")
        print(f"nivel requerido: {level}")
        print(f"nivel actual: {node.level}")
        if node.level >= level and node.program == None:
            if node.level == level and not node.reserved:
                print("Reservada la memoria")
                node.addProgram(program)
                return True
            elif node.level != level and node.bendicion_i != None and node.bendicion_i.program == None and node.bendicion_i.reserved == False:
                print("El hijo izquierdo no está reservado, vamos pa esa")
                return self.searchFreeMemory(node.bendicion_i,program,quantity)
            elif node.bendicion_d != None and (node.bendicion_d.program == None or node.bendicion_d.reserved == False):
                print("El hijo derecho no está reservado, vamos pa esa")
                return self.searchFreeMemory(node.bendicion_d,program,quantity)
            elif node.bendicion_i == None and node.level > 0:
                print("No tiene hijos")
                bendicion_i, bendicion_d = node.giveBirth(len(self.nodes))
                self.addNode(bendicion_i)
                self.addNode(bendicion_d)
                return self.searchFreeMemory(bendicion_i,program,quantity)
            else:
                print("No se que hace este caso")
                return self.searchFreeMemory(node.bendicion_i,program,quantity)
                print("fljfd")

        elif node.level >= level and node.reserved and node.program != None:
            if node.level == level and node.bendicion_i != None and node.bendicion_i.reservado:
                print("Voy al hermano derecho")
                return self.searchFreeMemory(node.pure.bendicion_d,program,quantity)
            elif node.level == level and node.bendicion_d != None and node.bendicion_d.reservado:
                print("Voy al tio")
                return self.searchFreeMemory(node.pure.pure.bendicion_d,program,quantity)
            
        elif node.level >= level and node.reserved:
            if node.bendicion_i != None and node.bendicion_i.program == None and node.bendicion_d.program == None and node.level == level:
                print("slfsao")
                node.addProgram(program)
            elif node.bendicion_d != None and node.bendicion_d.program == None and node.bendicion_d.reserved == False and node.level == level:
                print("es asi")
                node.addProgram(program)
            elif node.bendicion_d != None and node.bendicion_d.program == None:
                print("que")
                return self.searchFreeMemory(node.bendicion_d,program,quantity)
                #print("Probablemente no hay memoria disponible")
            else:
                print("por aqui")
                return False
                
        else:
            print("owos")
            return False

        """ while (node.level != level):
            # Si estamos en el nodo padre, verificamos que tenga hijos, y si nos tiene se le crean
            if node.reserved == False and level:
                print("Estamos en el papa del nivel que es?")
                # Si no tiene se le crean sus hijos
                if node.bendicion_i == None and level == node.level-1:
                    print("Holis va a dar a luz")
                    bendicion_i, bendicion_d = node.giveBirth()
                    self.searchFreeMemory(bendicion_i,program,quantity)
                    return True
                # Tiene hijos y el izquierdo esta ocupado
                elif node.bendicion_i != None and node.bendicion_i.reserved == True:
                    print("dkfldsafs")
                    # Se toma el derecho confirmando que no este en uso
                    if node.bendicion_d != None and node.bendicion_d.reserved == False:
                        bendicion_d.addProgram(program)
                        return True
                    # Se busca al tio
                    else:
                        print("Tio!!")
                        node = node.pure.bendicion_d
                        self.searchFreeMemory(node,program,quantity)
            elif node.level != level+1 and node.reserved == True:
                print("OWO")
                if node.bendicion_i.reserved == True and node.bendicion_d.reserved == True:
                    print("NO HAY ESPACIO???")
            elif node.level == level and node.reserved == True:
                print("UWU")
            else:
                print("djkfladjsaassaa24124912fsd") """

        """ elif node.level == level and node.reserved == True:
            node = node.pure
            self.searchFreeMemory(node.bendicion_d,program,quantity)
        else:
            if node.bendicion_i == None:
                bendicion_i, bendicion_d = node.giveBirth()
                print(bendicion_i.level)
                print(bendicion_d.level)
                if (not self.searchFreeMemory(bendicion_i,program,quantity)):
                    self.searchFreeMemory(bendicion_i,program,quantity)
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
        self.level = level
        self.reserved = False
        print(self)

    def addProgram(self,program):
        self.program = program
        pure = self.pure
        while pure != None:
            pure.reserved = True
            pure = pure.pure          
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
        if 0 < memory_size < 1024000 :
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