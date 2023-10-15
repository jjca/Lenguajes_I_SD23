import sys
import re

class Program:
    def __init__(self,name,language):
        self.name = name
        self.languages = [language]
    
    def addLanguage(self,language):
        self.languages.append(language)
    
    def getLanguages(self):
        return self.languages
    
    def getName(self):
        return self.name
    

class Interpreter:
    def __init__(self,base_language,language):
        self.base_language = base_language
        self.language = language

    def getBaseLanguage(self):
        return self.base_language
    
    def getDestLanguage(self):
        return self.language
    
class Translator:
    def __init__(self,base_language,origin_language,dest_language):
        self.base_language = base_language
        self.origin_language = origin_language
        self.dest_language = dest_language
    
class Language:
    def __init__(self,name):
        self.name = name

class Maquina():
    def __init__(self):
        self.supported_languages = ['local']
        self.executable_programs = []
        self.translators = [Translator('local','local','local')]
        self.programs = []
        self.interpreters = []


    def searchProgram(self,program_name,program_language):
        print(program_name)
        print(program_language)
        if len(self.programs) == 0:
            print("No hay programas definidos")
            return 0
        for prog in self.programs:
            if prog.getName() == program_name:
                if (program_language in prog.getLanguages()):
                    return 2
                else:
                    print("programe existe pero sin ese lenguaje")
                    print("adding lang")
                    prog.addLanguage(program_language)
                    return -1
        else:   
            print("El programa no existe")
            return 1

    """def twoInterpreterAddition(self,interpreter_a,interpreter_b):
        if (interpreter_a.getBaseLanguage != interpreter_b.getBaseLanguage and interpreter_a.getDestLanguage != interpreter_b.getDestLanguage):
            if (interpreter_a.getDestLanguage() == interpreter_b.getBaseLanguage()):
                self.addInterpreterToMachine(interpreter_a.getBaseLanguage(),interpreter_b.getDestLanguage())
            else:
                print("Interpreter language not supported")
        else:
            print("Same interpreter. Not adding") """

    def interpreterLoop(self,base_language,dest_language):
        old_list = self.interpreters.copy()
        
        new_interpreter = Interpreter(base_language,dest_language)
        # Si no existe el interprete lo añadimos
        if (not self.searchInterpreter(new_interpreter)):
            print(f"El interprete que entró ahorita se creará con {base_language} -> {dest_language}")
            """ El interprete se añade a maquina y si su lenguaje base es igual a uno soportado por la maquina entonces 
            el lenguaje de destino es soportado por la maquina """
            self.addInterpreterToMachine(new_interpreter)
            while old_list:
                # Se desempila un interprete de la lista vieja (la que no tiene al nuevo)
                interpreter_pop = old_list.pop(0)
                print(f"El interprete que se sacó tiene: {interpreter_pop.getBaseLanguage()}->{interpreter_pop.getDestLanguage()}")
                print(f"el interprete que se va a evaluar tiene {new_interpreter.base_language} -> {new_interpreter.getDestLanguage()}")
                print(f" aloooo{base_language} -> {dest_language}")
                
                # Si el lenguaje base del desempilado es igual al lenguaje de destino del nuevo  entonces
                # desempilado = (L0->L1)
                # nuevo = (L2 -> L0)
                # Y
                # el lenguaje base del nuevo pertenece a la lista de soportados
                # entonces se llama para ver si hay que crear un interprete (L2 -> L1)
                
                if (interpreter_pop.getBaseLanguage() == dest_language and base_language in self.supported_languages):
                    print("primer if")
                    self.interpreterLoop(base_language,interpreter_pop.getDestLanguage())
                    return True
        
                #Si el lenguaje de destino del desempilado es igual al lenguaje base del nuevo 
                #    desempilado = (L0->L1) 
                #    nuevo = (L1 -> L2)
                #    Y 
                #  el lenguaje base del desempilado pertenece a la lista de soportados
                #entonces se llama para ver si hay que crear un interprete (L0 -> L2)
                elif (interpreter_pop.getDestLanguage() == base_language and interpreter_pop.getBaseLanguage() in self.supported_languages):
                    print("segundo if")
                    self.interpreterLoop(interpreter_pop.getBaseLanguage(),dest_language)
                    return True              
            return True
        else:
            return False


    """    size_list_old = list_sizes
        while interpreters_stack_old:
            
            interpreters_stack.pop(0)
            print(f"El interprete nuevo es desde {new_interpreter.getBaseLanguage()} a {new_interpreter.getDestLanguage()}")
            print(f"el interprete en maquina es {machine_interpreter.getBaseLanguage()} a {machine_interpreter.getDestLanguage()}")
            if machine_interpreter.getDestLanguage() == new_interpreter.getBaseLanguage():
                print("bueno, el nuevo tiene un lenguaje base soportado por un destino ")
                if (self.searchInterpreter(machine_interpreter.getBaseLanguage(),new_interpreter.getDestLanguage())):
                    self.interpreterLoop(new_interpreter)
                elif (machine_interpreter.getBaseLanguage != new_interpreter.getBaseLanguage and machine_interpreter.getDestLanguage != new_interpreter.getDestLanguage):
                    self.searchInterpreter(machine_interpreter.getBaseLanguage(),new_interpreter.getDestLanguage())
                #self.twoInterpreterAddition(machine_interpreter,new_interpreter)
                else:
                    break
            else:
                if (self.searchInterpreter(new_interpreter.getBaseLanguage(),new_interpreter.getDestLanguage())):
                    break      
                    print("idk") """



    def addProgram(self,program_name,program_language):
        self.programs.append(Program(program_name,program_language))
        return True

    def addLanguageToProgram(self,program_name,program_language):
        for prog in self.programs:
            if prog.getName() == program_name:
                prog.addLanguage(program_language)
    
    def searchInterpreter(self,interpreter):
        for Interp in self.interpreters:
            if Interp.base_language == interpreter.getBaseLanguage() and Interp.language == interpreter.getDestLanguage():
                print("Interpreter already exists")
                return True
        else:
            return False
            
    def addInterpreterToMachine(self,new_interpreter):
        if new_interpreter.getBaseLanguage() in self.supported_languages and new_interpreter.getDestLanguage() not in self.supported_languages:
            self.supported_languages.append(new_interpreter.getDestLanguage())
        self.interpreters.append(new_interpreter)
            
    def searchTranslator(self,base_language,origin_language,dest_language):
        for trans in self.translators:
            if trans.base_language == base_language and trans.dest_language == dest_language and trans.origin_language == origin_language:
                print("Translator already exists")
                return True
        else:
            print("Traductor no existe")
            return False
    
    def addTranslator(self,base_language,origin_language,dest_language):
        self.translators.append(Translator(base_language,origin_language,dest_language))
        return True

    def checkIfExecutable(self,program_name):
        if len(self.programs) == 0:
            print("Lista vacia")
            return False
        for program in self.programs:
            if program_name == program.name:
                print(f"Revisando {program.getName()}")
                for lang in program.getLanguages():
                    if lang in self.supported_languages:
                        print(f"El lenguaje {lang} es soportado")
                        print(self.supported_languages)
                        return True
                print(f"El lenguaje {lang} NO es soportado")
                print(self.supported_languages)
                return False
            else: 
                print("coño?")
                print(f"{program_name}, {program.name}")
        return False
        
def main():
    LOCAL = Maquina()
    for line in sys.stdin:
        entrada = line.rstrip().split(" ")
        if 'salir' == line.rstrip().lower():
            break
        elif 'definir' == entrada[0].lower():
            if 'programa' == entrada[1].lower():
                if (LOCAL.searchProgram(entrada[2].lower(),entrada[3].lower()) == 0 or LOCAL.searchProgram(entrada[2].lower(),entrada[3].lower()) == 1):
                    if(LOCAL.addProgram(entrada[2].lower(),entrada[3].lower())):
                        print(f"Se definió el programa '{entrada[2]}', ejecutable en '{entrada[3]}'")
                    else:
                        print("error desconocido - programa")
                elif (LOCAL.searchProgram(entrada[2].lower(),entrada[3].lower()) == -1):
                    print(f"Se definió el programa '{entrada[2]}', ejecutable en '{entrada[3]}'")
                else:
                    print(f"El programa '{entrada[2]}', ejecutable en '{entrada[3]}' ya existe")

            elif 'interprete' == entrada[1].lower():
                if (LOCAL.interpreterLoop(entrada[2].lower(),entrada[3].lower())):
                    print(f"Se definió un intérprete para '{entrada[3]}', escrito en '{entrada[2]}'")
                else:
                    print(f"No se definió un intérprete para '{entrada[3]}', escrito en '{entrada[2]}'")

            elif 'traductor' == entrada[1].lower():
                if (not LOCAL.searchTranslator(entrada[2].lower(),entrada[3].lower(),entrada[4].lower())):
                    if(LOCAL.addTranslator(entrada[2].lower(),entrada[3].lower(),entrada[4].lower())):
                        print(f"Se definió un traductor de '{entrada[3]}' hacia '{entrada[4]}', escrito en '{entrada[2]}'")
                    else:
                        print("error desconocido - traductor")
                else:
                    print(f"El traductor de '{entrada[3]}' hacia '{entrada[4]}', escrito en '{entrada[2]}' ya existe")
        elif 'ejecutable' == entrada[0].lower():
            print(f"El nombre del programa es: {entrada[1]}")
            if (LOCAL.checkIfExecutable(entrada[1].lower())):
                print(f"El programa {entrada[1]} es ejecutable")
            else:
                print(f"El programa {entrada[1]} no es ejecutable")
        elif 'int' == entrada[0].lower():
            print("#############")
            for interpreter in LOCAL.interpreters:
                print(f"Interpretes: {interpreter.base_language} a: {interpreter.language}")
            print("#############")
        elif 'trad' == entrada[0].lower():
            print("#############")
            for trasl in LOCAL.translators:
                print(f"Traductor escrito en: {trasl.base_language} origen: {trasl.origin_language} hacia: {trasl.dest_language}")
            print("#############")
        elif 'prog' == entrada[0].lower():
            print("#############")
            for program in LOCAL.programs:
                print(f"Programa: {program.getName()} lenguajes: {program.getLanguages()}")
            print("#############")
        elif 'lang' == entrada[0].lower():
            print("#############")
            print(LOCAL.supported_languages)
            print("#############")
        else:
            print("Error de sintaxis vuelva a escribir")
    print("Exit")

if __name__ == "__main__":
    main()