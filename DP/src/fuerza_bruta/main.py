# Ejercicio Dinamica Codigo Fuerza Bruta

class Node:
    def __init__(self,index,value,color) -> None:
        self.index=index
        self.value=value
        self.color=color
    def __str__(self) -> str:
        return f"Node:  Index:{self.index}  Value:{self.value}  Color:{self.color}"
    def __repr__(self) -> str:
        return self.__str__()
    
        
class Manager:
    def __init__(self,a,b) -> None:
            self.lis:list[Node]=[]
            self.a=a
            self.b=b
            self.value=0
    def add(self,index,value,color):
        if len(self.lis)==0:
            self.lis.append(Node(index,value,color))
            self.value+=value*self.b
            return
        last=self.lis[-1]
       
        self.lis.append(Node(index,value,color))
            
        if last.color==color:#Multiplico por a
           self.value+=value*self.a 
        else:# Multiplico por b
            self.value+=value*self.b
    def __str__(self) -> str:
        return f"Value:{self.value} Nodes:{self.lis}"
    def __repr__(self) -> str:
        return self.__str__()
    def __gt__(self,other):
        return self.value>=other.value
import itertools

def generar_combinaciones(n):
    # Genera todas las combinaciones posibles de True/False de tamaño n
    combinaciones = list(itertools.product([True, False], repeat=n))
    return combinaciones


def solver(n,q,v,c):
    resultado = generar_combinaciones(n)

    for _ in range(q):
        a, b = map(int,input(f"Ingresa a y b separados por un espacio: ").split())
        chains:list[Manager]=[]
        for combinacion in resultado:
            manager=Manager(a=a,b=b)
            for i in range(n):
                if not combinacion[i]:
                    continue
                manager.add(index=i,value=v[i],color=c[i])
            chains.append(manager)
        chains=sorted(chains,reverse=True)
        #print(chains)
        print(f"El mayor valor es {chains[0].value}")
if __name__=="__main__":

    n, q = map(int, input("Ingresa n y q separados por un espacio: ").split())
    v = list(map(int, input(f"Ingresa {n} valores para v separados por espacios: ").split()))
    c = list(map(int, input(f"Ingresa {n} valores para c separados por espacios: ").split()))
    solver(n,q,v,c)
