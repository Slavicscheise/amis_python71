def Min(list):
    if len(list) == 1:
        return list[0]
    else:
        return min(Min(list[:-1]), list[-1])  

print(Min(input("Введите список через пробел: ").split())) 
