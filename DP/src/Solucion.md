El problema trata explicitamente de que subsecuencia puedo tomar tal que maximice el valor.
Entonces si se pudieran generar todas las subsecuencias posibles entonces se pudiera encontrar cuales son las óptimas
- En nuestro caso cualquier subsecuencia optima tiene el mismo valor por lo que todo elemento del cjto optimo global es optimo igual.
- Pueden existir multiples optimos :
Para $a=5$ y $b=1$

| v     | 1   | 1   | 1   | 1   |
| ----- | --- | --- | --- | --- |
| c     | 1   | 2   | 1   | 2   |
| index | 0   | 1   | 2   | 3   |
El maximo puede ser con  0-2-3  o 0-1-3 que es 7
 
 

## Observaciones
- Si tenemos una bola que al multiplicar con *a* o *b*  esta da un valor $< 0$ $\Rightarrow$ que esa bola (Si es que la ultima antes de añadir es del mismo color o no) no puede ser añadida 
- El valor maximo global todos los factores de las bolas tienen que ser positivos.
- Un valor de cero de una bola no afecta si esta al fin al de la cadena maxima pero si puede influir por estar en el medio, dado que puede ser que la siguiente bola sea de color analogo haciendo que esta esta en la cadena máxima.
-

## Solucion Fuerza Bruta
Si generamos todas las subcadenas posibles entonces podemos saber cuales nos dan el maximo y tomar este valor, El algoritmo seria similar a generar todas las cadenas binarias, dado que es analogo a poner esa bola como ultima en la secuencia.
- Esta solucion es exponencial por tanto no es eficiente ni cerca de serlo
### Podas
- Se puede pensar no añadir una bola esta dado por el valor multiplicado por a o b lo que corresponda es $< 0$ descartaria casos los cuales no llevan al optimo pero, en ciertos casos es necesario por ejemplo:

	| 1   | -2  | 1   | 4   | 0   | -1  | v     |
	| --- | --- | --- | --- | --- | --- | ----- |
	| 1   | 2   | 1   | 2   | 1   | 1   | c     |
	| 0   | 1   | 2   | 3   | 4   | 5   | index |
	Para $a=2$ y $b=1$ 
	Escoger los indices 0-1-8 es conveniente 
	- Esto se debe a que el valor máximo si la subsecuencia termine con el color c es $-\infty$ dado que nunca se ha escogido ese color.
	- Si ya ese color ha tenido alguna representacion en alguna subcadena explorada entonces poner un negativo después de multiplicar con $a$ o $b$ no puede llevar a una solucion óptima 




# Ideas con respecto optimizar la solucion
- Si te tiene una bola de color c[i] que con alguna antecesora de color c[i-1] mejora el valor que tendria terminando la secuencia en ese color y que no fuera esa bola.
- Si una bola tiene valor $=0$
	- Al ser un problema de decision (Annadir esta o no al final de la subcadena) puede afectar valor optimo
	- El valor de esta bola en caso de annadirse o no puede afectar a las proximas bolas y no puede ser predecido solamente con la informacion de las bolas vistas hasta ese momento

- No importa en que momento se este siempre se puede tener por cada color cual seria el cjto de subsecuencias maximas hasta el momento (Donde todas las subsecuencias maximas tienen igual valor).
- Se puede considerar por cada color cual seria el valor maximo de la cadena que termine con ese color en cada momento 
## Algoritmos propuestos para optimizar en tiempo polinomial.
Dado que llevamos las subsecuencias optimas (Una subsecuencia optima por cada color) hasta la bola i podemos para cada color posible conocer si es conveniente annadir esa bola con la ultima bola de esa subsecuencia

### Algoritmo en  $o\left(n\cdot c\right)$ c=Cantidad de colores:
#### Idea
- Supongamos que tenemos por cada color se tiene guardado cual es el valor maximo de todas las cadenas hasta el momento que terminan con ese color (Se guarda  en $c[i]$ )
- Si recorremos el array de bolas y por cada bola determinamos si el valor maximo de nuestro color es menor que unirnos con alguna subsecuencia que termine en algun color.

#### Demostracion
Dado que el problema lo hemos resumido a que cada vez que seleccionamos una bola miramos cual es la bola que la debe de preceder (De ahi tener guardados los máximos por colores)
Cuando vemos cual seria a que color debe machearse entre todos comparamos si este valor es mayor que el que tenemos con nuestro propio color de ser mayor pues actualizamos
Sea:
-  El color de x $c[x]$ 
- $A$ la subsecuencia maxima del color de x que se tenia hasta el elemento x con valor $val[A]$
Supongamos que para todos los colores $\ne c\left\lbrack x\right\rbrack$ el máximo de las subsecuencias con dichos colores($maxSeq$) $+ valor[x]$ $\ge val\left\lbrack A\right\rbrack\Rightarrow val\left\lbrack A\right\rbrack=maxSeq$ 
 Entonces es evidente que siempre estamos buscando en cada indice las mayor subsecuencia que termina con cada color por tanto al finalizar el mayor valor de estos es el valor a dar




## Algoritmo en  $O\left(n\right)$
### Notación 
- $Max_1$ Valor que se lleva para conocer el valor de las cadenas optimas maximas que se tienen hasta el momento osea $Max_1=$valor que tiene cualquier cadena que este en el maximo hasta ese momento
- $Max_2$ Valor que se lleva para conocer el 2do mejor valor de las cadenas optimas hasta ese momento 
- $v[i]$ valor de la bola $i$
### Idea:
 Siguiendo la idea anterior ahora en trataremos de no tener que recorrer todos los colores.
 - Dado que en cada iteración solo nos interesa conocer el valor que tienen las subcadenas optimas que terminan en dichos colores, 
	 - osea si dos colores sus subcadenas optimas( hasta el momento) terminan en igual valor entonces a nuestros efectos son igual el valor
	  - Se va guardado ese valor del maximo de todas las subcadenas optimas hasta el momento una una variable $Max_1$ , entonces todas las cadenas que sus colores cumplan con ellos tendran que ver si es mas conveniente machearse con esa subcadena optima del color o con alguna que tienen el *2do * mejor valor los cuales se representan mediante la variable $Max_2$ 
		  - Osea si la bola que ahora tenemos que decidir si puede conformar o no el proximo subglobal tiene que  comprobar lo siguiente: 
			  - Si la bola su color pertenece a los que si valor es $Max_1$:
				  -  $Max_1 +a\cdot v\left\lbrack i\right\rbrack$ donde $v\left\lbrack i\right\rbrack$ es el valor de esa bola
				  - $Max_2 +b\cdot v\left\lbrack i\right\rbrack$ , $Max_2$ dado que se queria machear con alguna subcadena que este en el 2 mejor valor hasta ese elemento
					  - se compara el maximo entre el maximo hasta ese momento del color de i y lo que da los dos puntos anteriores, y si son mayores que $Max_1$ se actualiza este.
			 - Si la bola su color no tiene cadena suboptima en $Max_1$:
				 - Se elije el maximo entre lo que se tenia de maximo en ese color y:
					 - Machearla con una cadena de las de $Max_1$
					 - O machearla con una de su mismo color
### Demostración:
Supongamos que estamos en la bola $i$ en ella conocemos todas las cadenas que su valor optimo es el maximo hasta este indice que estan en un cjto $A$ , como $A$ tiene las cadenas que tienen el valor maximo todas las cadenas de $A$ tienen igual valor: $Max_1$ 
Si hasta el momento se tiene:

 

| Mejor valor hasta el momento | 4   | 3   | 1   | 3   | 4   |
| ---------------------------- | --- | --- | --- | --- | --- |
| indice del color             | 1   | 2   | 3   | 4   | 5   |
$Max_1=4$ y $A=$ {Mejor cadena del color 1 y Mejor cadena del color 5}
Análogamente tenemos a $B$ que tiene las cadenas que tiene los *2do* mejores colores osea:
$B=$ {Mejor cadena del color 2 y Mejor cadena del color 4} y $Max_2=3$

Siempre tenemos el mejor valor( $Max_1$) y el *2do*  mejor valor ($Max_2$ )hasta el momento.

Sea la bola i de color $c_i$.
Supongamos que $c_i$ tiene cadena en A.
- 


