import re
class commandIncomplete(Exception):
    "Comando incompleto"
    pass
class commandWrongSyntax(Exception):
    "El comando está incorrecto"
    pass

def evalPrefijo(string):
    stack = []
    for elem in string[::-1]:
        if re.match(r"[0-9]+",elem):
            stack.append(elem)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            operador = elem
            if operador == "/":
                operador = "//"
            res = eval(num1+""+""+operador+""+""+num2)
            stack.append(str(res))
    print(stack[0])

def evalPostfijo(string):
    stack = []
    for elem in string:
        if re.match(r"[0-9]+",elem):
            stack.append(elem)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            operador = elem
            if operador == "/":
                operador = "//"
            res = eval(num2+""+""+operador+""+""+num1)
            stack.append(str(res))
    print(stack[0])

def transPreToIn(string):
    stack = []
    dictPrec = {"+":"1","-":"1","*":"2","/":"2"}
    conmutativos = ["+","*"]
    for elem in string[::-1]:
        if re.match(r"[0-9]+",elem):
            stack.append((elem,None))
        else:
            expr1, operadorExpr1 = stack.pop()
            expr2, operadorExpr2 = stack.pop()
            operador = elem
            if operadorExpr1 is not None and dictPrec.get(operador) > dictPrec.get(operadorExpr1): 
                expr1 = "("+expr1+")"
            if operadorExpr2 is not None and dictPrec.get(operador) > dictPrec.get(operadorExpr2): 
                expr2 = "("+expr2+")"
            if operadorExpr2 is not None and dictPrec.get(operador) == dictPrec.get(operadorExpr2) and operador not in conmutativos: 
                expr2 = "("+expr2+")"
            newexpr = expr1+operador+expr2
            stack.append((newexpr,operador))
    print(newexpr)

def transPostToIn(string):
    stack = []
    dictPrec = {"+":"1","-":"1","*":"2","/":"2"}
    conmutativos = ["+","*"]
    for elem in string:
        if re.match(r"[0-9]+",elem):
            stack.append((elem,None))
        else:
            expr2, operadorExpr2 = stack.pop()
            expr1, operadorExpr1 = stack.pop()
            operador = elem
            if operadorExpr1 is not None and dictPrec.get(operador) > dictPrec.get(operadorExpr1): 
                expr1 = "("+expr1+")"
            if operadorExpr2 is not None and dictPrec.get(operador) > dictPrec.get(operadorExpr2): 
                expr2 = "("+expr2+")"
            if operadorExpr2 is not None and dictPrec.get(operador) == dictPrec.get(operadorExpr2) and operador not in conmutativos: 
                expr2 = "("+expr2+")"
            newexpr = expr1+operador+expr2
            stack.append((newexpr,operador))
    print(newexpr)

def main():
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
                                evalPrefijo(entrada[2:])
                            elif 'post' == orden:
                                evalPostfijo(entrada[2:])
                            else:
                                raise ValueError
                        except commandWrongSyntax:
                            continue
                    else:
                        raise commandIncomplete
                except commandIncomplete:
                    print("Faltan argumentos en el comando EVAL")
                    continue
                except commandWrongSyntax:
                    print("El comando está incorrecto")
                    continue
            elif 'mostrar' == entrada[0].lower():
                try:
                    if len(entrada) > 3:
                        orden = entrada[1].lower()
                        try: 
                            if 'pre' == orden:
                                print("Prefijo")
                                transPreToIn(entrada[2:])
                            elif 'post' == orden:
                                print("postfijo")
                                transPostToIn(entrada[2:])
                            else:
                                raise ValueError
                        except commandWrongSyntax:
                            continue
                    else:
                        raise commandIncomplete
                except commandIncomplete:
                    print("Faltan argumentos en el comando MOSTRAR")
                    continue
                except commandWrongSyntax:
                    print("El comando está incorrecto")
                    continue
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