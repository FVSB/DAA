#include <stdio.h>

#define MAX_SIZE 100010

typedef long long ll;

// Función para obtener el máximo entre dos números
ll max(ll a, ll b) {
    return a > b ? a : b;
}

int main() {
    int n, q; // Número de elementos y consultas
    ll c[MAX_SIZE], v[MAX_SIZE], dp[MAX_SIZE];

    // Leer el número de elementos y consultas
    scanf("%d%d", &n, &q);

    // Leer los valores de v y c
    for (int i = 1; i <= n; i++) {
        scanf("%I64d", &v[i]);
    }
    for (int i = 1; i <= n; i++) {
        scanf("%I64d", &c[i]);
    }

    // Procesar cada consulta
    while (q--) {
        int a, b; // Variables para almacenar los valores de la consulta
        scanf("%d%d", &a, &b);

        // Inicializar el arreglo dp con un valor muy bajo
        for (int i = 1; i <= n; i++) {
            dp[i] = (ll)-1e15;
        }

        int ca = 0, cb = 0; // Índices para almacenar los mejores resultados

        // Calcular el mejor resultado para cada consulta
        for (int i = 1; i <= n; i++) {
            ll as = max(dp[c[i]] + v[i] * a, dp[cb] + v[i] * b);

            // Si ca no es igual a c[i], se evalúa una opción adicional
            if (ca != c[i]) {
                as = max(as, dp[ca] + v[i] * b);
            }

            // Actualizar los índices ca y cb según el nuevo valor as
            if (ca != c[i]) {
                if (dp[ca] < as) {
                    cb = ca;
                    ca = c[i];
                } else if (dp[cb] < as) {
                    cb = c[i];
                }
            }

            // Actualizar el valor en dp[c[i]]
            dp[c[i]] = max(dp[c[i]], as);
        }

        // Imprimir el resultado para la consulta actual
        printf("%I64d\n", dp[ca]);
    }

    return 0;
}