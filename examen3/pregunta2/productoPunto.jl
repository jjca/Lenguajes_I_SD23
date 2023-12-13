using Distributed
using Base.Threads
n = 100_000_000
x = rand(n)
y = rand(n)

function productoPuntoD(x,y) 
    suma = 0
    @distributed (+) for i in 1:n
        suma += x[i]*y[i]
    end
    return suma
end

function productoPunto(x,y) 
    suma = 0
    for i in 1:n
        suma += x[i]*y[i]
    end
    return suma
end


@time println(productoPunto(x,y))
@time println(productoPuntoD(x,y))