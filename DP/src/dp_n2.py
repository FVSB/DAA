import sys
# Definiciones de constantes
N = int(1e5) + 20
INF = int(1e15)
 
# Lectura de entrada
# input para el codeforces 
#n, q = map(int, sys.stdin.readline().split())
#v = list(map(int, sys.stdin.readline().split()))
#c = list(map(int, sys.stdin.readline().split()))
# Input normal para entrada mas comoda
#n, q = map(int, input("Ingresa n y q separados por un espacio: ").split())
#v = list(map(int, input(f"Ingresa {n} valores para v separados por espacios: ").split()))
#c = list(map(int, input(f"Ingresa {n} valores para c separados por espacios: ").split()))
n=4
q=1
v=[-3, 6, -1, 2]
c=[1, 2, 3, 1]
N=max(c)+1
#dp=[-INF]*N
#color_can=[False]*len(dp)
for _ in range(q):
    #a, b = map(int,input(f"Ingresa a y b separados por un espacio: ").split())
    #a, b = map(int, sys.stdin.readline().split())
    a=1
    b=-1
    # Limpiar otra vez la memoria
    dp=[-INF]*(N)
    color_can=[False]*len(dp)
    
    for i in range(n): # Por cada elemento
        ci=c[i]
        last=dp[ci]
       
        for col in range(1,len(dp)): # Por cada color
            
            if col == ci and color_can[ci]:
                
                s=last if last>-INF else 0
                dp[ci]=max(dp[ci],s+(a*v[i])) #Ver el maximo entre ponerme yo ahora como ultima bola de mi color
            else:# Si no soy la ultima bola entonces ver si a lo mejor en alguna que era otro colr
                s=dp[col] if dp[col]>-INF else 0
                dp[ci]=max(dp[ci],s+(b*v[i]))
                #dp[ci]=max(dp[ci],dp[col]+b*v[i])
        dp[ci]=max(dp[ci],b*v[i])# Siempre hay que preguntar si soy yo el primer numero de la subsecuencia mejora
        color_can[ci]=True
            
    print(max(max(dp),0))
      
            


