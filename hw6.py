class Animal:
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