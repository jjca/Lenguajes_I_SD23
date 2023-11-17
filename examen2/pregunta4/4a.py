def main():
    print(elJojeNacci(10))
    print(elJojeNacci(20))
    print(elJojeNacci(30))
    print(elJojeNacci(60))

    for i in range(0,55):
        print(f"i = {i} F(i) = {elJojeNacci(i)}")
    for i in range(1,50):
        print(f"i ={i}, F({i}) - F({i-1}): {elJojeNacci(i)-elJojeNacci(i-1)}")

    #print(f"Fibo {fib(50)}")
    print(f"el de 34: {tailJojeNacci(34)}")
    print(f"el de 35: {tailJojeNacci(35)}")

    print(f"el de 36: {tailJojeNacci(36)}")
    print(f"el de 37: {tailJojeNacci(37)}")
    print(f"el de 38: {tailJojeNacci(38)}")
    print(f"el de 39: {tailJojeNacci(39)}")

    print(f"el de 90: {elJojeNacci(5)}")
    print(f"el de 90: {tailJojeNacci(200)}")

    print("Iterativos")
    print(f"el de 24: {jojeNacciIter(24)}")
    print(f"el de 35: {jojeNacciIter(200)}")

def elJojeNacci(n):
    if n < 0:
        print("error")
    elif 0 <= n < 35:
        return n
    else:
        return elJojeNacci(n-7) + elJojeNacci(n-14) + elJojeNacci(n-21) + elJojeNacci(n-28) + elJojeNacci(n-35)
    
def fib(n):
    def go(n,a =0,b=1):
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return go(n-1,b,a+b)
    return go(n)
            
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


def jojeNacciIter(n):
    lalistik = list(range(35))
    suma = 0
    i = 0
    for i in range(n):
        lalistik.append(lalistik[28]+lalistik[21]+lalistik[14]+lalistik[7]+lalistik[0])
        lalistik = lalistik[1:]
    return lalistik[0]


if __name__ == "__main__":
    main()