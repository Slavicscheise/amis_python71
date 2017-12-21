def maximum_count(list, iterator, sum):
    if iterator == -1:
        return sum
    elif list[iterator] == max(list):
        sum += 1
    return maximum_count(list, iterator - 1, sum)


def integer(list, iterator):
    if iterator == -1:
        return
    list[iterator] = int(list[iterator])
    return integer(list, iterator - 1)


list = input("Введите список: ").split()
integer(list, len(list) - 1)
print(maximum_count(list, len(list) - 1, 0))
