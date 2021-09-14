"""Необходимо дополнить "Практическое задание №6" таким образом,
чтобы в конце программы мы вызвали статический метод
родительского класса Animal, который вывел бы нам количество всех созданных экземпляров."""

class Animal:

    counter = 0

    def __init__(self):
        Animal.counter += 1

    @classmethod
    def get_counter(cls):
        return cls.counter


    def voice(self):
        pass



#Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
class Dog(Animal):
    def voice(self):
        print('Woof')

class Cat(Animal):
    def voice(self):
        print('Meow')

class Cow(Animal):
    def voice(self):
        print('Mooooooooooooooooooo')

#Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

cow = Cow()
cat = Cat()
dog = Dog()

cow.voice()
cat.voice()
dog.voice()

print(Animal.get_counter())