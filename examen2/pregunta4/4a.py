def main():
    print(elJojeNacci(10))
    print(elJojeNacci(20))
    print(elJojeNacci(30))
    print(elJojeNacci(60))

    for i in range(0,50):
        print(f"i = {i} F(i) = {elJojeNacci(i)}")



    for i in range(1,50):
        print(f"i ={i}, F({i}) - F({i-1}): {elJojeNacci(i)-elJojeNacci(i-1)}")

    #print(f"Fibo {fib(50)}")
    print(f"el de 34: {tailJojeNacci(34)}")
    print(f"el de 35: {tailJojeNacci(35)}")


    print("Iterativos")
    print(f"el de 24: {jojeNacciIter(24)}")
    print(f"el de 35: {jojeNacciIter(35)}")

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
    def ayudante(a = 0, b = 1, i = 0):
        if i == n:
            return a
        else:
            return ayudante(b,a+b,i+1)
    return ayudante(n)

def jojeNacciIter(n):
    suma = 0
    if n < 0:
        print("error")
    elif 0 <= n < 35:
        return n+suma
    else:
        for i in range(0,7):
            if i == 7:
                suma = 7*suma
            else:
                suma = suma
        return suma

if __name__ == "__main__":
    main()