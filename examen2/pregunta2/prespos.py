import re

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

class commandIncomplete(Exception):
    "Comando incompleto"
    pass

class commandWrongSyntax(Exception):
    "El comando está incorrecto"
    pass

def evalPrefijo(string):
    stack = []
    print(f"string oriignal {string}")
    for elem in string[::-1]:
        if re.match(r"[0-9]+",elem):
            print(f"{elem} es un numero")
            stack.append(elem)
        else:
            print(f"{elem} es un operador")
            num1 = stack.pop()
            num2 = stack.pop()
            operador = elem
            res = eval(num2+""+""+operador+""+""+num1)
            print(f"olaaa {res}")
            stack.append(str(res))
    print(stack)

def evalPostfijo(string):
    stack = []
    print(f"string oriignal {string}")
    for elem in string:
        if re.match(r"[0-9]+",elem):
            print(f"{elem} es un numero")
            stack.append(elem)
        else:
            print(f"{elem} es un operador")
            num1 = stack.pop()
            num2 = stack.pop()
            operador = elem
            res = eval(num2+""+""+operador+""+""+num1)
            print(f"olaaa {res}")
            stack.append(str(res))
    print(stack)

def main():
    print("Hola")
    activo = True
    while activo:
        entrada = list(input("Introduzca una opción válida. Para más información escriba HELP:  ").split())
        try:
            if 'salir' == entrada[0].lower() and len(entrada) == 1:
                activo = False
                break
            elif 'eval' == entrada[0].lower():
                try:
                    if len(entrada) > 3:
                        orden = entrada[1].lower()
                        try: 
                            if 'pre' == orden:
                                print("Prefijo")
                                evalPrefijo(entrada[2:])
                            elif 'post' == orden:
                                print("postfijo")
                                evalPostfijo(entrada[2:])
                            else:
                                raise ValueError
                        except memoryNoAvailable:
                            print("uwu")
                            continue
                    else:
                        raise commandIncomplete
                    """elif len(entrada[2].lower()) == 0 or len(entrada) < 3:
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
                        continue"""
                except commandIncomplete:
                    print("Faltan argumentos en el comando EVAL")
                    continue
                except commandWrongSyntax:
                    print("El comando está incorrecto")
                    continue
            elif 'mostrar' == entrada[0].lower():
                print("Memoria en uso:")
            elif 'help' == entrada[0].lower() and len(entrada) == 1:
                print("\nLos siguientes comandos están disponibles:")
                print("EVAL <orden> <expr>: Evalúa la expresión dada en la notación indicada. Orden puede ser PRE o POST")
                print("MOSTRAR <orden> <expr>: Muestra la expresion dada en notación infija. Orden puede ser PRE o POST")
                print("HELP: muestra este mensaje")
                print("SALIR: sale del programa")
            else:
                raise ValueError
        except ValueError:
            print("El comando es incorrecto o está incompleto")
            continue

if __name__ == "__main__":
    main()