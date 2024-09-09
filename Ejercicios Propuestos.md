
## Greedy: 
## Descripción:
Dada una cuadrícula de tamaño $n \times n$  y un arreglo $(a)$ de tamaño $(n$), en la fila $(i$), las primeras $(a_i$) celdas son negras y las restantes son blancas. Puedes realizar dos operaciones:
1. Pintar de blanco un subcuadro de ($2 \times 2$).
2. Pintar de blanco toda una fila.

El objetivo es encontrar el número mínimo de operaciones necesarias para hacer que todas las celdas sean blancas.


## DP:

Hay *n* bolas. Están dispuestas en una fila. Cada bola tiene un color (para conveniencia, un número entero) y un valor entero. El color de la *i*-ésima bola es $c_i$ y el valor de la *i*-ésima bola es $v_i$.
La ardilla Liss elige algunas bolas y forma una nueva secuencia sin cambiar el orden relativo de las bolas. Ella quiere maximizar el valor de esta secuencia.
El valor de la secuencia se define como la suma de los siguientes valores para cada bola (donde *a* y *b* son constantes dadas): 

- Si la bola no está al principio de la secuencia y el color de la bola es el mismo que el de la bola anterior, suma (el valor de la bola ) x *a* .
- De lo contrario, suma(el valor de la bola) x *b*.


Se te dan *q* consultas. Cada consulta contiene dos enteros $a_i$ y $b_i$ . Para cada consulta, encuentre el valor máximo de la secuencia que puede crear cuando $a=a_i$ y $b=b_i$ .



Ten en cuenta que la nueva secuencia puede estar vacía, y el valor de una secuencia vacía se define como cero.



## NP:
    3-Dimensional Matching