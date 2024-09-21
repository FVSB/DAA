= Descripcion del problema <descripcion-del-problema>
Sean los conjuntos $X$ $Y$ $Z$: - $X sect Y sect W = nothing$ \
- $lr(|X|) = lr(|Y|) = lr(|W|) = q$ Sea $M subset.eq W$ x $X$ x $Y$

Existe un matching en M Osea \$\\exists M^\`\\subseteq M\$ tal que: - \$\\left|M^{\`}\\right|\=q\$ - $forall a in W union X union Y$ $a$ esta en alguna terceta de \$M^\`\$ sin repetir ninguno.

= INsertar ejemplo <insertar-ejemplo>
== Pasos a realizar: <pasos-a-realizar>
- Demostrar que 3-DM es NP
- Seleccionar un problema NP-Completo para reducirlo (En este caso 3-Sat)
  - Demostrar que dicha transformacion es en tiempo polinomial

=== 3-DM es NP: <dm-es-np>
Dada una instancia$lr((M , X , Y , W))$ del 3-DM se construye un algoritmo no determinista que genere una solución de $lr(|W|)$ tercetas de $M$ y compruebe en tiempo polinomial que no hay dos tercetas con elementos comunes.

=== Reducir: <reducir>
- 3 SATISFABILITY (3SAT)
  - Instancia:
    - Conjunto de m cláusulas C \= {c1, …, cm}
      - $lr(|c_i|)$ \= 3 , 1 ≤ i ≤ m
    - Sobre un conjunto finito de n variables booleanas
      - $U = u_1 , . . . , u_n$
- Pregunta: Existe aluna asignación válida de $U$ que satisfaga todas las cláusulas de $C$. \#\#\#\# Notación

#figure(
  align(
    center,
  )[#table(
      columns: 2,
      align: (col, row) => (auto, auto,).at(col),
      inset: 6pt,
      [3-Sat],
      [3-DM],
      [Variables: $u_1 . . . u_n$],
      [Variables: $u_i lr((j))$,$b_i lr((j))$, $S_x lr((j))$, $G_y lr((j))$],
      [Literales: $u_1$ $not u_1$],
      [Variables: $u_i$ , $not u_i lr((j))$],
      [Cláusulas:$C_j = lr((u_1 , not u_2 , u_3))$],
      [Tercetas $C_j lr(
          {lr((u_1 lr((j)) , S_x lr((j)) , S_y lr((j)))) , lr((not u_2 lr((j)) , S_x lr((j)) , S_y lr((j)))) , lr((u_3 , S_x lr((j)) , S_y lr((j))))}
        )$],
    )],
)

=== Construcción de los componentes: <construcción-de-los-componentes>
La demostración se basa en la construcción de tres tipos de componentes: - Componentes de #emph[asignación] - Componentes de #emph[satisfacción] - Componentes de #emph[recolección]

==== Componentes de asignación: <componentes-de-asignación>
- Para cada variable $u_i in U$ se introduce una componente $T_i$.
  - $T_i$ depende del número de cláusulas m de C
- Estructura de $T_i$:
  - Elementos internos:
    - ai \[j\] Є X, 1 ≤ j ≤ m ; bi \[j\] Є Y, 1 ≤ j ≤ m
      - No van a pertenecer a otras tercetas de otro Ti
  - Elementos externos:
    - ui \[j\] , ⌐ui \[j\] Є W, 1 ≤ j ≤ m
- Pueden pertenecer a otras tercetas Nota: El literal $u_i$ en 3SAT puede ser usado en varias cláusulas, en el 3-DM debemos tener muchas m copias de $u_i$.

=== Insertar diagrama <insertar-diagrama>
==== Insertar diagramas explicativos <insertar-diagramas-explicativos>
==== Componentes de satisfacción: <componentes-de-satisfacción>
- Para cada cláusula cj Є C introducimos una componente Cj.
- Estructura:
  - Elementos Internos: sx \[j\] Є X, sy \[j\] Є Y : 1 ≤ j ≤ m
  - Elementos externos: ui \[j\] , ⌐ui \[j\] Є W : 1 ≤ i ≤ n;1 ≤ j ≤ m
- Cj \= {\(ui \[j\], sx \[j\], sy \[j\]): si el literal ui Є cj} U {\(⌐ui \[j\], sx \[j\], sy \[j\]): si el literal ⌐ui Є cj}

= INsertar diagrama <insertar-diagrama-1>
Cualquier matching \$M^{\`}\\subseteq M\$ debe contener una terceta de $C_j$ para emparejar los elementos internos $S_x lr([j])$ y $S_y lr([j])$: - Sx \[j\] y Sy \[j\] pueden ser emparejados, sí sólo sí, al menos uno de los literales (ui) de cj no ha sido emparejado en alguna componente "Truth seeting" Ti (Ti ∩ M’) - Si tenemos una 3SAT-Instancia satisfacible, entonces las variables Sx\[j\] y Sy\[j\] pueden ser emparejadas - Si tenemos una 3SAT-Instancia no satisfacible, entonces las variables Sx\[j\] y Sy\[j\] no pueden ser emparejadas.

==== Componente de recolección: <componente-de-recolección>
Hay muchos$u_i lr([j])$ que no se emparejan con componentes de #emph[asignación] ni con componentes de #emph[satisfacción]

- Hay $m times n$ variables $u$ sin emparejar después de calcular las tercetas de asignación.
- Si todas las $m$ cláusulas se satisfacen se han emparejado $m$ variables.
- Finalmente quedan sin emparejar $lr((m times n)) - m = m lr((n - 1))$

Se introduce $m lr((n - 1))$ variables nuevas: - $g_x lr([k]) in X$, $g_y lr([k]) in Y : 1 lt.eq k lt.eq m lr((n - 1))$

Cada pareja ($g_x lr([k])$, $g_y lr([k])$) se enlazará con una única variable $u_i lr([j])$ o $⌐ u_i lr([j])$ que no estén en las tercetas que se han formado con las componentes anteriores:

= Insertar imagen <insertar-imagen>
= Resumiendo: <resumiendo>
- $W = lr(
    {u_i lr([j]) , not u_i lr([j]) : 1 lt.eq i lt.eq n , 1 lt.eq j lt.eq m}
  )$
- $X = A union S_x union G_x$ ($2 m n$)
  - $A = lr({a_i lr([j]) : 1 lt.eq i lt.eq n , 1 lt.eq j lt.eq m})$
  - $S_x = lr({s_x lr([j]) : 1 lt.eq j lt.eq m})$
  - $G_x = lr({g_x lr([j]) : 1 lt.eq j lt.eq m lr((n - 1))})$
- $Y = B sect S_y union G_y$ $lr((2 m n))$
  - $B = lr({b_i lr([j]) : 1 lt.eq i lt.eq n , 1 lt.eq j lt.eq m})$
  - $S_y = lr({s_y lr([j]) : 1 lt.eq j lt.eq m})$
  - $G_y = lr({g_y lr([j]) : 1 lt.eq j lt.eq m lr((n - 1))})$ $M = lr((union))$

= Insertar formualq que dice a que es igual M <insertar-formualq-que-dice-a-que-es-igual-m>
#figure(align(center)[#table(
    columns: 2,
    align: (col, row) => (auto, auto,).at(col),
    inset: 6pt,
    [Significado],
    [Enumeración],
    [Cantidad de variables en $< U , C >$],
    [$n$],
    [Cantidad de clausulas en $< U , C >$],
    [$m$],
    [Cantidad de componentes de #emph[asignación] triple en $M$],
    [$2 m n$],
    [Cantidad de componentes de #emph[asignación] triple en \$M^\`\$],
    [$m n$],
    [Cantidad de componentes de #emph[satisfacción] triple en $M$],
    [$3 m$],
    [Cantidad de componentes de #emph[satisfacción] triple en \$M^\`\$],
    [$m$],
    [Cantidad de componentes #emph[recolección] en $M$],
    [$2 m^2 n lr((n - 1))$],
    [Cantidad de componentes #emph[recolección] en \$M^\`\$],
    [$m lr((n - 1))$],
    [Cardinalidad del emparejamiento perfecto],
    [$2 m n$],
    [Cardinalidad de $M$],
    [$2 m n = 3 m = 2 m^2 n lr((n - 1))$],
  )])

= Insertar tabla ejemplo <insertar-tabla-ejemplo>
- Se ha observado que las tercetas resultantes $M$ son el producto cartesiano de $W times X times Y$ \
- Esta forma de definir las tercetas:
  - Desde su definición en términos de una instancia (U,C) del 3SAT
  - $M$ se construye en tiempo polinomial.

= Demostrar que si $M$ contiene un matching \$M^\`\$ ssi (U,C) es satisfacible <demostrar-que-si-m-contiene-un-matching-m-ssi-uc-es-satisfacible>
== Si (U,C) es satisfacible entonces \$M^{\`}\\subset M\$ es un matching <si-uc-es-satisfacible-entonces-msubset-m-es-un-matching>
- Sea $t : U$ —-\>$lr({T , F})$ EL dominio de valores para $U$ que satisface las cláusulas $C$.
- Se construye un matching \$M^{\`}\\subseteq M\$ del modo siguiente:
  - $Z_j in lr({u_i , not u_i ; 1 lt.eq i lt.eq n}) sect c_j$
    - Literales con asignación verdadera.
    - Debe de existir al menos uno, ya que $t$ satisface a $c_j$.
- Se construye la \$M^\`\$: - Insertar la formula - \$G^\`:\$ conjunto de $m lr((n - 1))$ tercetas de g que incluyen: - todos los $g_x lr([k])$ $in X$ , $g_y lr([k]) in Y$ - Y los $u_i lr([j]) in , not u_i lr([j]) in W$ que no se han emparejado.
  - Es fácil de verificar que siempre se puede construir un \$G^\`\$ para que el resultado del conjunto \$M^\`\$ sea un matching. \#\# Si \$M^{\`}\\subseteq M\$ es un matching entonces $lr((U , C))$ es satisfacible.
- Se ha visto que para cada $u_i in U$, \$M^\`\$ incluía exactamente $m$ tercetas de $T_i : T_i^t or T_i^f$
- Sea $t :$ $U$ –\> $T , F$ donde $t lr((u_i)) =$\$ \$T ssi M^\`\\cap T\_{i}\=T\_{i}^{t}\$
  - $t$ será una asignación correcta que satisface $C$.
- Consideremos una cláusula arbitraria $c_j in C$
  - Para cubrir los elementos internos de la componente $C_j$:
    - Se necesita al menos una terceta de $C_j$ contenida en \$M ^\`\$
    - Esta terceta contiene un literal de $c_j in C$, que no estará en \$M^{\`}\\cap T\_{i}\$
- Como $t lr((u_i)) =$ $T$ $s s i$ \$M^{\`}\\cap T\_{i}\=T\_{i}^{t}\$
  - Entonces $t$ satisface la cláusula $c_j$
- Si todas las cláusulas $c_j in C$ se satisfacen:
  - $lr((U , C))$ es satisfacible. 
