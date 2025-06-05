def addintegers(x,y):
    return x + y
addintegers(10, 11)

print("""
      Welcome, Ali!
      Welcome, Ben!
      Welcome, Cat!
      Welcome, Doge!
      Welcome, Eggbert!
      Welcome, Fred!
      Welcome, Grod!
      """)


class Animal:
    def __init__(self, name):
        self.sound = ""
        self.name = name

    def make_sound(self):
        print(f'{self.name} goes {self.sound}')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "woof"

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.sound = "meow"

class Cow(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.sound = "moo"


animals = [Dog('Dog'), Cat('Cat'), Cow('Cow')]
for a in animals:
    a.make_sound()




words = ["hello", "world", "!"]
sentence = words[0] + ' ' + words[1] + words[2]
print(sentence)


fruit_stock = ["apple", "banana", "cherry"]
for i, item in enumerate(fruit_stock):
    print(i, item)