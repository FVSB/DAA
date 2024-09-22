## Codigo del dp en O(n)
## Este si funciona en codeforces
#https://codeforces.com/contest/264/submission/281751718 link a donde acerto
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
n, q = map(int, input("Ingresa n y q separados por un espacio: ").split())
v = list(map(int, input(f"Ingresa {n} valores para v separados por espacios: ").split()))
c = list(map(int, input(f"Ingresa {n} valores para c separados por espacios: ").split()))

N=max(c)+1
# Ajustamos los índices de c para que empiecen desde 0
c = [x - 1 for x in c]

# Procesamiento de consultas
for _ in range(q):
    # Para el codeforces
    #a, b = map(int, sys.stdin.readline().split())
    a, b = map(int,input(f"Ingresa a y b separados por un espacio: ").split())
    mx1 = 0
    mx2 = 0
    
    ans = [-INF] * N  # Inicializamos el arreglo ans con -INF

    for i in range(n):
        if mx1 == ans[c[i]]:
            ans[c[i]] = max(ans[c[i]], ans[c[i]] + a * v[i])
            ans[c[i]] = max(ans[c[i]], mx2 + b * v[i])
            mx1 = max(mx1, ans[c[i]])
        else:
            ans[c[i]] = max(ans[c[i]], ans[c[i]] + a * v[i])
            ans[c[i]] = max(ans[c[i]], mx1 + b * v[i])
            mx2 = max(mx2, ans[c[i]])
            
            if mx2 > mx1:
                mx1, mx2 = mx2, mx1

    print(mx1)