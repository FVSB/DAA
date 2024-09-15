
## Greedy : 
ErnKor está listo para hacer cualquier cosa por Julen, incluso nadar a través de pantanos infestados de cocodrilos. Decidimos poner a prueba este amor. ErnKor tendrá que nadar a través de un río con un ancho de 1 metro y una longitud de n metros.

El río está muy frío. Por lo tanto, en total (es decir, durante toda la natación desde 0 hasta n+1) ErnKor puede nadar en el agua no más de k metros. Por el bien de la humanidad, hemos añadido no solo cocodrilos al río, sino también troncos sobre los que puede saltar. Nuestra prueba es la siguiente:

Inicialmente, ErnKor está en la orilla izquierda y necesita llegar a la orilla derecha. Estas se encuentran a 0 y n+1 metros respectivamente. El río se puede representar como n segmentos, cada uno con una longitud de 1 metro. Cada segmento contiene un tronco 'L', un cocodrilo 'C' o solo agua 'W'. ErnKor puede moverse de la siguiente manera:

Determina si ErnKor puede llegar a la orilla derecha.


La primera línea de cada caso de prueba contiene tres números n, m, k (0 ≤ k ≤ 2 · 10^5, 1 ≤ n ≤ 2 · 10^5, 1 ≤ m ≤ 10) — la longitud del río, la distancia que ErnKor puede saltar y el número de metros que ErnKor puede nadar sin congelarse.

La segunda línea de cada caso de prueba contiene una cadena a de longitud n. a_i denota el objeto ubicado en el i-ésimo metro. (a_i ∈ {'W','C','L'})


- Se está en la superficie (osea, en la orilla o en un tronco), no puede saltar hacia delante mas de m ($1<=m<=10$) metros (Puede saltar a la orilla a un tronco o al agua).
- Si esta en el agua solo puede nadar hasta el siguiente segmento de rio (o hasta la orilla si esta en el agua si el agua esta a n-*th* metros)
- ErnKor no puede aterrizar en un segmento con un cocodrilo de ninguna manera
#### Determine si ErnKor puede llegar a la orilla correcta.
## DP :

Hay *n* bolas. Están dispuestas en una fila. Cada bola tiene un color (para conveniencia, un número entero) y un valor entero. El color de la *i*-ésima bola es $c_i$ y el valor de la *i*-ésima bola es $v_i$.
La ardilla Liss elige algunas bolas y forma una nueva secuencia sin cambiar el orden relativo de las bolas. Ella quiere maximizar el valor de esta secuencia.
El valor de la secuencia se define como la suma de los siguientes valores para cada bola (donde *a* y *b* son constantes dadas): 

- Si la bola no está al principio de la secuencia y el color de la bola es el mismo que el de la bola anterior, suma (el valor de la bola ) x *a* .
- De lo contrario, suma(el valor de la bola) x *b*.


Se te dan *q* consultas. Cada consulta contiene dos enteros $a_i$ y $b_i$ . Para cada consulta, encuentre el valor máximo de la secuencia que puede crear cuando $a=a_i$ y $b=b_i$ .



Ten en cuenta que la nueva secuencia puede estar vacía, y el valor de una secuencia vacía se define como cero.



## NP:
    3-Dimensional Matching