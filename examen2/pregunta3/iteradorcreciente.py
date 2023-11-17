from itertools import combinations

def obtenerCrecientes(lista):
    crecientes = []
    for i in range(0,len(lista)):
        if(all(lista[i][j] <= lista[i][j + 1] for j in range(len(lista[i])-1))):
            crecientes.append(lista[i])
            print(f"{lista[i]}")


def obtenerParticiones(lista):
    particiones = list()
    for i in range(len(lista)+1):
        particiones += list(combinations(lista,i))
    return particiones    

def main():
    print("Se tiene la lista:")
    lista = [1,4,3,2,5]
    print(lista)
    particiones = obtenerParticiones(lista)
    crecientes = obtenerCrecientes(particiones)
    print(crecientes)

if __name__ == "__main__":
    main()