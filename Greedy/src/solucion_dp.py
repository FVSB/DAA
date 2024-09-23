from collections import deque

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    s = input()
    #n, m, k = map(int,sys.stdin.readline().split()) Codeforces
    #s = list(sys.stdin.readline().split()) Codeforces
    dp = [-1] * (n + 2)
    dp[0] = k
    
    for i in range(1, n + 2):# De primera casilla a orilla
        if i != n + 1 and s[i - 1] == 'C': # Si esto en la orilla derecha o hay un cocodrilo no actualizo
            continue
        
        for t in range(1, m + 1):# Trato de actualiza si hubo un tronco  o la orilla izq anterior a mi
            if i - t >= 0 and (i - t == 0 or s[i - t - 1] == 'L'):
                dp[i] = max(dp[i], dp[i - t])
        
        if i > 1 and s[i - 2] == 'W': 
            dp[i] = max(dp[i], dp[i - 1] - 1)
    
    if dp[n + 1] >= 0:
        print("YES")
    else:
        print("NO")