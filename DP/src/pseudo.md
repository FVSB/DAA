INICIO

DEFINIR MAX_SIZE COMO 100010
DECLARAR c[MAX_SIZE], v[MAX_SIZE], dp[MAX_SIZE] COMO ENTEROS LARGOS

FUNCIÓN max(a, b):
    SI a > b ENTONCES
        RETORNAR a
    SINO
        RETORNAR b

LEER n, q // Número de elementos y consultas

PARA i DESDE 1 HASTA n HACER:
    LEER v[i]

PARA i DESDE 1 HASTA n HACER:
    LEER c[i]

MIENTRAS q NO SEA CERO HACER:
    LEER a, b // Valores de la consulta

    PARA i DESDE 1 HASTA n HACER:
        dp[i] ASIGNAR -10^15

    ca ASIGNAR 0
    cb ASIGNAR 0

    PARA i DESDE 1 HASTA n HACER:
        as ASIGNAR max(dp[c[i]] + v[i] * a, dp[cb] + v[i] * b)

        SI ca NO ES IGUAL A c[i] ENTONCES:
            as ASIGNAR max(as, dp[ca] + v[i] * b)

        SI ca NO ES IGUAL A c[i] HACER:
            SI dp[ca] < as ENTONCES:
                cb ASIGNAR ca
                ca ASIGNAR c[i]
            SINO SI dp[cb] < as ENTONCES:
                cb ASIGNAR c[i]

        dp[c[i]] ASIGNAR max(dp[c[i]], as)

    IMPRIMIR dp[ca]

FIN