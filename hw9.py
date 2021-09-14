"""Необходимо создать два параллельных потока, каждый из которых выводил бы
на экран числа от 10 до 1 в обратном порядке с интервалом в одну секунду.
В выводе должно быть понятно какая нить выполняется, и когда каждая из них
начинает и заканчивает своё выполнение."""

import time
from threading import Thread

def mycounter(name, interval):

    for x in range(10):
        print(name + str(10-x) + ' ')
        time.sleep(interval)
        if 10-x == 1:
            print(name + 'закончил работу')

thread1 = Thread(target=mycounter, args=('Первый поток: ', 1,))
thread2 = Thread(target=mycounter, args=('Второй поток: ', 1,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()