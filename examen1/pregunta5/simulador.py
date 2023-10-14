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
        self.languages = ['local']
        self.executable_programs = []
        self.translators = [Translator('local','local','local')]
        self.programs = []
        self.interpreters = [Interpreter('local','local')]


    def searchProgram(self,program_name,program_language):
        print(program_name)
        print(program_language)
        if len(self.programs) == 0:
            print("si lista vacia")
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
            print("chao")
            return 1
    
    def addProgram(self,program_name,program_language):
        self.programs.append(Program(program_name,program_language))
        return True

    def searchInterpreter(self,base_language,dest_language):
        for Interp in self.interpreters:
            if Interp.base_language == base_language and Interp.language == dest_language:
                print("Interpreter already exists")
                return True
        else:
            print("Interprete no existe")
            return False
            
    def addInterpreter(self,base_language,dest_language):
        self.interpreters.append(Interpreter(base_language,dest_language))
        return True
            
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
                if (not LOCAL.searchInterpreter(entrada[2].lower(),entrada[3].lower())):
                    if(LOCAL.addInterpreter(entrada[2].lower(),entrada[3].lower())):
                        print(f"Se definió un intérprete para '{entrada[3]}', escrito en '{entrada[2]}'")
                    else:
                        print("error desconocido - interprete")
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
            print("por hacer")
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
        else:
            print("Error de sintaxis vuelva a escribir")
    print("Exit")

if __name__ == "__main__":
    main()