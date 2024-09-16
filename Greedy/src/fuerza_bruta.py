inf=float("inf")
#'W','C','L'
def min_steps(n:int,m:int,k:int,arr:list[str])->float:
    
    min_safe=inf
    for val in arr:
        if val in ["C",'c']: # Es que hay un cocodrilo por tanto no se puede avanzar
            return inf
        if val in ['W','w']: # Es que hay agua por tanto se continua avanzando
            min_safe= min_safe+1 if min_safe<inf else 1
        else:
            next_choise=min_steps(n,m,k,arr,)
            