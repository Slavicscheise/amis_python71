x1=float(input("Введите х первой координаты: "))
y1=float(input("Введите у первой координаты: "))
x2=float(input("Введите х второй координаты: "))
y2=float(input("Введите у второй координаты: "))

def distense(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5


print(distense(x1,y1,x2,y2))
