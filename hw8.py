"""Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и создать
на его основе новый файл, где содержимое будет записано в обратном порядке.
В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке."""

with open('myfile.txt', 'r') as f1:
    words = f1.read()

with open('myfile2.txt', 'w+') as f2:
    for line in reversed(list(words)):
        f2.write(line)

print('Первый файл: \n ' )

with open('myfile.txt') as f3:
    for item in f3.readlines():
        print(item)

print('')
print('Второй файл записан обратно первому. Поэтому если снова прочитать его задом наперед, он будет идентичен первому. \n')
with open('myfile2.txt') as f4:
    output = f4.readlines()
    new_list = []

    for item in reversed(output):
        new_list.append(item)

    for item in new_list:
        print (item[::-1])





