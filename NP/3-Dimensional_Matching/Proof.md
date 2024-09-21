# Descripcion del problema

Sean los conjuntos $X$ $Y$ $Z$:
-  $X\cap Y\cap W=∅$  
-  $|X|=|Y|=|W|=q$
Sea $M\subseteq W$ x $X$ x $Y$ 

Existe un matching en M
Osea $\exists M^`\subseteq M$ tal que:
- $\left|M^{`}\right|=q$
- $\forall a\in W\cup X\cup Y$ $a$ esta en alguna terceta de $M^`$ sin repetir ninguno.

# INsertar ejemplo


## Pasos a realizar:
- Demostrar que 3-DM es NP
- Seleccionar un problema NP-Completo para reducirlo (En este caso 3-Sat)
	- Demostrar que dicha transformacion es en tiempo polinomial


### 3-DM es NP:
Dada una instancia$(M, X, Y, W)$ del 3-DM se
construye un algoritmo no determinista que
genere una solución de $| W |$ tercetas de $M$ y
compruebe en tiempo polinomial que no hay
dos tercetas con elementos comunes.

### Reducir:
- 3 SATISFABILITY (3SAT)
	- Instancia:
		- Conjunto de m cláusulas C = {c1, ..., cm}
			- $| c_i |$ = 3 , 1 ≤ i ≤ m
		- Sobre un conjunto finito de n variables booleanas
			- $U = {u_1, ..., u_n}$ 
-  Pregunta:
	 Existe aluna asignación válida de $U$ que satisfaga todas
		las cláusulas de $C$. 
#### Notación 

| 3-Sat                                            | 3-DM                                                                                                                                                                                                                                                  |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variables: ${u_1 ... u_n}$                       | Variables: $u_i(j)$,$b_i(j)$, $S_x(j)$, $G_y(j)$                                                                                                                                                                                                      |
| Literales: $u_1$ $\lnot u_1$                     | Variables: $u_i$  , $\lnot u_{i}\left(j\right)$                                                                                                                                                                                                       |
| Cláusulas:$C_{j}=\left(u_1,\lnot u_2,u_3\right)$ | Tercetas $C_{j}\left\lbrace\left(u_1\left(j\right),S_{x}\left(j\right),S_{y}\left(j\right)\right),\left(\lnot u_2\left(j\right),S_{x}\left(j\right),S_{y}\left(j\right)\right),\left(u_3,S_{x}\left(j\right),S_{y}\left(j\right)\right)\right\rbrace$ |

### Construcción de los componentes: 
La demostración se basa en la construcción de tres tipos de
componentes:
- Componentes de *asignación*
- Componentes de *satisfacción* 
- Componentes de *recolección* 

#### Componentes de asignación:
- Para cada variable $u_{i}\in U$ se introduce una
componente $T_i$. 
	- $T_i$ depende del número de cláusulas m de C
- Estructura de $T_i$:
	- Elementos internos:
		- ai [j] Є X, 1 ≤ j ≤ m ; bi [j] Є Y, 1 ≤ j ≤ m
			- No van a pertenecer a otras tercetas de otro Ti
	- Elementos externos:
		- ui [j] , ⌐ui [j] Є W, 1 ≤ j ≤ m
- Pueden pertenecer a otras tercetas
 Nota: El literal $u_i$ en 3SAT puede ser usado en varias cláusulas, en
el 3-DM debemos tener muchas m copias de $u_i$.

### Insertar diagrama 

#### Insertar diagramas explicativos

#### Componentes de satisfacción:
- Para cada cláusula cj Є C introducimos una componente Cj.
- Estructura:
	- Elementos Internos: sx [j] Є X, sy [j] Є Y : 1 ≤ j ≤ m
	- Elementos externos: ui [j] , ⌐ui [j] Є W : 1 ≤ i ≤ n;1 ≤ j ≤ m
-  Cj = {(ui [j], sx [j], sy [j]): si el literal ui Є cj} U {(⌐ui [j], sx [j], sy [j]): si el literal ⌐ui Є cj}


# INsertar diagrama


Cualquier matching $M^{`}\subseteq M$ debe contener una terceta
de $C_j$ para emparejar los elementos internos $S_{x}\left\lbrack j\right\rbrack$ y $S_{y}\left\lbrack j\right\rbrack$: 
- Sx [j] y Sy [j] pueden ser emparejados, sí sólo sí, al menos uno de los literales (ui) de cj no ha sido emparejado en alguna componente “Truth seeting” Ti (Ti ∩ M')
- Si tenemos una 3SAT-Instancia satisfacible, entonces las variables Sx[j] y Sy[j] pueden ser emparejadas
- Si tenemos una 3SAT-Instancia no satisfacible, entonces las variables Sx[j] y Sy[j] no pueden ser emparejadas.



#### Componente de recolección:
Hay muchos$u_{i}\left\lbrack j\right\rbrack$ que no se emparejan con componentes
de *asignación* ni con componentes de *satisfacción*

- Hay $m\times n$ variables $u$ sin emparejar después de calcular las tercetas de asignación.
- Si todas las $m$ cláusulas se satisfacen se han emparejado $m$ variables.
- Finalmente quedan sin emparejar $\left(m\times n\right)-m=m\left(n-1\right)$

Se introduce $m\left(n-1\right)$ variables nuevas:
- $g_{x}\left\lbrack k\right\rbrack\in X$, $g_{y}\left\lbrack k\right\rbrack\in Y:1\le k\le m\left(n-1\right)$

Cada pareja ($g_x [k]$, $g_y [k]$) se enlazará con una
única variable $u_i [j]$ o $⌐u_i [j]$ que no estén en las
tercetas que se han formado con las componentes
anteriores:

# Insertar imagen


# Resumiendo:
- $W=\left\lbrace u_{i}\left\lbrack j\right\rbrack,\lnot u_{i}\left\lbrack j\right\rbrack:1\le i\le n,1\le j\le m\right\rbrace$
- $X=A\cup S_{x}\cup G_{x}$ ($2mn$)
	- $A=\left\lbrace a_{i}\left\lbrack j\right\rbrack:1\le i\le n,1\le j\le m\right\rbrace$
	- $S_{x}=\left\lbrace s_{x}\left\lbrack j\right\rbrack:1\le j\le m\right\rbrace$
	- $G_{x}=\left\lbrace g_{x}\left\lbrack j\right\rbrack:1\le j\le m\left(n-1\right)\right\rbrace$
- $Y=B\cap S_{y}\cup G_{y}$       $(2mn)$ 
	- $B=\left\lbrace b_{i}\left\lbrack j\right\rbrack:1\le i\le n,1\le j\le m\right\rbrace$
	- $S_{y}=\left\lbrace s_{y}\left\lbrack j\right\rbrack:1\le j\le m\right\rbrace$
	- $G_{y}=\left\lbrace g_{y}\left\lbrack j\right\rbrack:1\le j\le m\left(n-1\right)\right\rbrace$
	$M=\left(\cup\right)$

# Insertar formualq que dice a que es igual M


| Significado                                                 | Enumeración                    |
| ----------------------------------------------------------- | ------------------------------ |
| Cantidad de variables en $<U,C>$                            | $n$                            |
| Cantidad de clausulas en $<U,C>$                            | $m$                            |
| Cantidad de componentes de *asignación* triple en $M$       | $2mn$                          |
| Cantidad de componentes de *asignación* triple en $M^`$     | $mn$                           |
| Cantidad de componentes de *satisfacción* triple en $M$     | $3m$                           |
| Cantidad de componentes de  *satisfacción*  triple en $M^`$ | $m$                            |
| Cantidad de componentes *recolección* en $M$                | $2m^2n\left(n-1\right)$        |
| Cantidad de componentes *recolección* en $M^`$              | $m\left(n-1\right)$            |
| Cardinalidad del emparejamiento perfecto                    | $2mn$                          |
| Cardinalidad de $M$                                         | $2mn=3m=2m^2n\left(n-1\right)$ |



# Insertar tabla ejemplo


- Se ha observado que las tercetas resultantes $M$ son el producto cartesiano de $W\times X\times Y$  
- Esta forma de definir las tercetas:
	- Desde su definición en términos de una instancia (U,C) del 3SAT
	- $M$ se construye en tiempo polinomial. 



# Demostrar que si $M$ contiene un matching $M^`$    ssi (U,C) es satisfacible


## Si (U,C) es satisfacible entonces $M^{`}\subset M$ es un matching
- Sea $t:U$ ---->$\left\lbrace T,F\right\rbrace$ EL dominio de valores para $U$ que satisface las cláusulas $C$. 
- Se construye un matching $M^{`}\subseteq M$ del modo siguiente:
	- $Z_{j}\in\left\lbrace u_{i},\lnot u_{i};1\le i\le n\right\rbrace\cap c_{j}$
		- Literales con asignación verdadera.
		- Debe de existir al menos uno, ya que $t$ satisface a $c_j$.
- Se construye la $M^`$:
	-  Insertar la formula
	- $G^`:$ conjunto de $m(n-1)$ tercetas de g que incluyen:
		- todos los $g_x[k]$ $\in X$ , $g_{y}\left\lbrack k\right\rbrack\in Y$
		- Y los $u_{i}\left\lbrack j\right\rbrack\in,\lnot u_{i}\left\lbrack j\right\rbrack\in W$ que no se han emparejado.
	- Es fácil de verificar que siempre se puede construir un $G^`$ para que el resultado del conjunto $M^`$ sea un matching.
## Si $M^{`}\subseteq M$ es un matching entonces $(U,C)$ es satisfacible.
- Se ha visto que para cada $u_{i}\in U$, $M^`$ incluía exactamente $m$ tercetas de $T_{i}:T_{i}^{t}\lor T_{i}^{f}$
- Sea $t:$ $U$ --> ${T,F}$ donde $t(u_i)=$$ $T ssi M^`\cap T_{i}=T_{i}^{t}$ 
	- $t$ será una asignación correcta que satisface $C$.
- Consideremos una cláusula arbitraria $c_{j}\in C$
	- Para cubrir los elementos internos de la componente $C_j$:
		- Se necesita al menos una terceta de $C_j$ contenida en $M ^`$
		- Esta terceta contiene un literal de $c_{j}\in C$, que no estará en $M^{`}\cap T_{i}$ 
- Como $t(u_i)=$ $T$ $ssi$  $M^{`}\cap T_{i}=T_{i}^{t}$
	- Entonces $t$ satisface la cláusula $c_j$
- Si todas las cláusulas $c_{j}\in C$ se satisfacen:
	- $(U,C)$ es satisfacible.