def obtenerCrecientes(lista):
    crecientes = []
    for i in range(0,len(lista)):
        if(all(lista[i][j] <= lista[i][j + 1] for j in range(len(lista[i])-1))):
            crecientes.append(lista[i])
            #print(f"{lista[i]}")
    return crecientes

def obtenerParticiones(lista):
    if lista == []:
        yield []
    else:
        for x in obtenerParticiones(lista[1:]):
            yield x
            yield [lista[0],*x]

def main():
    print("Se tiene la lista:")
    lista = [1,4,3,2,5]
    particiones= []
    print(lista)
    for x in obtenerParticiones(lista):
        particiones.append(x)
    #print(particiones)
    crecientes = obtenerCrecientes(particiones)
    print(crecientes)

if __name__ == "__main__":
    main()