inf=float("inf")
#'W','C','L'
def min_steps(n,m:int,arr:list[str],i:int)->float:
    # O es que llegue a la otra orilla
    min_safe=inf
    if m>n:# Esto es porque se puede saltar desde orilla a orilla
        return 0
    if len(arr)<=i:
        return 0
    val=arr[i]
   
    if val in ["C",'c']: # Es que hay un cocodrilo por tanto no se puede avanzar
        return -inf
    if val in ['W','w']: # Es que hay agua por tanto se continua avanzando
        l=i+1
        return 1+min_steps(n,m,arr,l)
    else: # Es que estoy en la orilla o un tronco
        for j in range(1,m+1):# Tratar de saltar lo maximo
            l=i+j
            next_choise=min_steps(n,m,arr,l)
            if next_choise==0:return 0 # Es que se llego  la otra orilla
            min_safe=min(min_safe,next_choise)
    return min_safe

def solve(n:int,m:int,k:int,arr:list[str]):
    """
    n: Cant de celdas
    m: Cant de metros que puede salta
    k: Cant de metros que puede nadar sin congelarse
    arr: El mapa
    """
    min_st=min_steps(n,m,arr,0)
    print(f"La cantida de pasos minima es {min_st}")
    if min_st==0:
        print("Se llego a la costa sin nadar")
    elif min_st ==-inf:
        print("No hubo forma de esquivar los cocodrilos")   
    return min_st!=-inf and k>=min_st

if __name__=="__main__":
    n,m,k  = map(int, input("Ingresa n (Cant de celdas) m (Cant de metros a saltar) k (Cant de metros a nadar): ").split())
    arr=str(input("Introduzca el mapa: ").split())
    arr=arr[2:]
    arr=arr[:-2]
    arr="-"+arr
    a=len(arr)
    print(solve(n,m,k,arr))