using Distributed
using Base.Threads
n = 10_000_000
# Genera vector de enteros entre 1 y 9999 de largo n.
#x = rand(1:9999,n)
#y = rand(1:9999,n)
# Genera vector de tamaño n de punto flotante
x = rand(n)
y = rand(n)

function productoPuntoPF(x,y) 
    suma = Threads.Atomic{Float64}(0);
    # Para enteros: suma = Threads.Atomic{Int}(0); 
    Threads.@threads for i in 1:n
        Threads.atomic_add!(suma,x[i]*y[i])
    end
    return suma[]
end

function productoPuntoPE(x,y) 
    suma = Threads.Atomic{Int}(0); 
    Threads.@threads for i in 1:n
        Threads.atomic_add!(suma,x[i]*y[i])
    end
    return suma[]
end

@everywhere function productoPuntoD(x,y) 
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



println("Número de hilos: ",nthreads())

println("Punto flotante")
@time println("productoPuntoPF ",productoPuntoPF(x,y))
@time println("productoPunto ",productoPunto(x,y))
@time println("productoPuntoD ",productoPuntoD(x,y))

println("Enteros")
x = rand(1:9999,n)
y = rand(1:9999,n)
@time println("productoPuntoPE ",productoPuntoPE(x,y))
@time println("productoPunto ",productoPunto(x,y))
@time println("productoPuntoD ",productoPuntoD(x,y))