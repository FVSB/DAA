def run() -> None:
    n,m,k = map(int, input().split())
    A = input()
    logs = [i for i in range(n) if A[i] == "L"] # Enumera donde están los troncos
    logs.append(n+1) # Añade el final como si fuera un tronco
    i = -1
    next_log = 0
    while i < n-1:# Ciclo while pq se irá saltando através de los troncos
        if m >= logs[next_log] - i:# Si el siguiente tronco esta a a una distancia cruzable se salta a el
            i = logs[next_log] # actualizar i hasta el tronco mas cercano
        else:
            i+=m # Saltar hasta el lugar saltable más cercano
            if i > n-1:# Si estoy en la orilla puedo decir que es cruzable
                print("YES")
                return
            while i < n and i < logs[next_log]: # Mientras i no este en la orilla y ademas no este en el siguiente tronco a nadar
                if A[i] != "C" and k > 0:
                    i+=1
                    k-=1
                else:# Si no puedo nadar o hay un cocodrilo que no puedo saltar digo que no se puede realizar el salto
                    print("NO")
                    return
        next_log +=1 # Voy hasta el siguiente tronco
    print("YES")
 
for _ in range(int(input())):
    run()