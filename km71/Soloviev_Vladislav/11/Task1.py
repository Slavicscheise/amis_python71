x = int(input("Введiть довжину списку - "))
listNumbers = []

'''
Користувач вводить кiлькiсть елементiв списку, та створюеться порожнiй список listNumbers
'''

def form_list(x):
    global listNumbers
    if len(listNumbers) < x:
        listNumbers.append(int(input("Введiть число - ")))
        form_list(x)
    else:
        return listNumbers

form_list(x)

'''
Створюеться, та, в подальшому, викликаеться функцiя form_list, що додае введенi користувачем числа до listNumbers,
да дiе допоки його довжина менше нiж кiлькiсть елементiв
'''

def minimum(listNumbers):
    if len(listNumbers) == 0:
        return
    if len(listNumbers) == 1:
        return listNumbers[0]
    min_elem = minimum(listNumbers[1:])
    if min_elem < listNumbers[0]:
        return min_elem
    else:
        return listNumbers[0]
'''
Створюеться рекурсивна функцiя minimum, що повертае нiчого, якщо довжина list_numbers = 0, перший (та единий)
елемент списку, коли довжина listN5umbers = 1. Якщо бiльше одного, то пробiгае по всiм елементам, шляхом
зменшення списку на елемент при кожному виклику функцii, та порiвнюе елементи, i виводить найменший.
'''

print("Мiнiмальний елемент списку -",minimum(listNumbers))
