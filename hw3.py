numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

#Вывести все нечетные числа больше 50, используя функцию filter().

def myFilter(x):
    if (x%2 != 0) and (x>50):
        return 1
    else:
        return 0

l = list(filter(myFilter, numbers))
print(l)

