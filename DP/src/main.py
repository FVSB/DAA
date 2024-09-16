def max(a, b):
    return a if a > b else b

def main():
    X = 100010
    c = [0] * X
    v = [0] * X
    dp = [-float('inf')] * X

    n, q = map(int, input().split())
    
    for i in range(1, n + 1):
        v[i] = int(input())

    for i in range(1, n + 1):
        c[i] = int(input())

    for _ in range(q):
        a, b = map(int, input().split())
        
        # Reiniciar dp para cada consulta
        dp = [-float('inf')] * X
        ca = cb = 0
        
        for i in range(1, n + 1):
            as_value = max(dp[c[i]] + v[i] * a, dp[cb] + v[i] * b)
            if ca != c[i]:
                as_value = max(as_value, dp[ca] + v[i] * b)
            
            if ca != c[i]:
                if dp[ca] < as_value:
                    cb = ca
                    ca = c[i]
                elif dp[cb] < as_value:
                    cb = c[i]
                    
            dp[c[i]] = max(dp[c[i]], as_value)

        print(dp[ca])

if __name__ == "__main__":
    main()