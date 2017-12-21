list1=[]
list2=[]
def inputl(n):
    if n==0:
        return list1
    else:
        element = int(input("ведите элемент: "))
        list1.append(element)
        return inputl(n-1)
def func(list2):
    return list2[::-1]
n = int(input("введите длину"))
list2 = inputl(n)
print (func(list2))
