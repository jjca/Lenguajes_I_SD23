import time
def main():
    for i in range(35,105,10):
            start_time = time.time()
            print(f"i = {i} F(i) = {tailJojeNacci(i)}")
            print("timepo: %s segundos" % (time.time()-start_time))

    for i in range(105,1000,100):
            start_time = time.time()
            print(f"i = {i} F(i) = {tailJojeNacci(i)}")
            print("timepo: %s segundos" % (time.time()-start_time))

    for i in range(35,105,10):
            start_time = time.time()
            print(f"i = {i} F(i) = {jojeNacciIter(i)}")
            print("timepo: %s segundos" % (time.time()-start_time))

    for i in range(105,1006,100):
            start_time = time.time()
            print(f"i = {i} F(i) = {jojeNacciIter(i)}")
            print("timepo: %s segundos" % (time.time()-start_time))

"""
Pregunta 4a.
Recibe un número n del cual retorna recursivamente 
F(n-7) + F(n-14) + F(n-21) + F(n-28) + F(n-35)
"""
def elJojeNacci(n):
    if n < 0:
        print("error")
    elif 0 <= n < 35:
        return n
    else:
        return elJojeNacci(n-7) + elJojeNacci(n-14) + elJojeNacci(n-21) + elJojeNacci(n-28) + elJojeNacci(n-35)
    
"""
Función dada definida como recursiva de cola.
En este caso recibe un n y retorna el valor
"""            
def tailJojeNacci(n):
    lalistik = list(range(35))
    def tailJojeNacciAux(n, i, lalistik):
        if i == n:
            return lalistik[0]
        else:         
            lalistik.append(lalistik[28]+lalistik[21]+lalistik[14]+lalistik[7]+lalistik[0])
            lalistik = lalistik[1:]
            return tailJojeNacciAux(n, i+1, lalistik)
    return tailJojeNacciAux(n,0,lalistik)

"""
Función de ejecución de recursión de cola iterativa.
Se trasladó el append de la lista y simplemente se itera sobre esta hasta obtener el resultado.
"""
def jojeNacciIter(n):
    lalistik = list(range(35))
    i = 0
    for i in range(n):
        lalistik.append(lalistik[28]+lalistik[21]+lalistik[14]+lalistik[7]+lalistik[0])
        lalistik = lalistik[1:]
    return lalistik[0]


if __name__ == "__main__":
    main()