CustumerInput=input('Введите список через пробел')

def ListCreator(Str,i):
    if i+1==len(Str):
        return [Str]  
    if Str[i]==' ':
        return [Str[:i]]+ ListCreator(Str[i+1:],0)
    else:
        return ListCreator(Str,i+1)

def Min(List):
    if len(List)==1:
        return List[0]
    
    if List[0]>=List[1]:
        del(List[1])
    else:
        del(List[1])        
    return Min(List)

CustumerList=ListCreator(CustumerInput,0)
print(Min(CustumerList))
