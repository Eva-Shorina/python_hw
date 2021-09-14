
dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

'''Составить из него новый словарь, который будет содержать только 
те элементы, у которых значение больше или равно 3.'''

dict2 = dict.copy()

for k in dict:
    if dict[k] < 3:
        del dict2[k]

for k in dict2:
    print (k, dict[k])