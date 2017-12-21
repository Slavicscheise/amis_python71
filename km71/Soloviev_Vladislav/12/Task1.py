numbers=input("введите числа:").split()
max=int(numbers[0])
def last_max(list, n,i,lmax,max):
    if(i==n):
        return lmax
    else:
        if((int)(max)<(int)(list[i])):
            lmax=max
            max=list[i]
        return last_max(list, n,i+1, lmax,max)
print(last_max(numbers, len(numbers),0,max,max))
