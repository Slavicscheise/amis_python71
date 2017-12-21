def power(a,n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)
a=float(input("Введите a:"))
n=int(input("Введите n:"))
print(power(a,n))
