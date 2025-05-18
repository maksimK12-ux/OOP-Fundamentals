class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def get_sound(self):
        print(f'I am a {self.name} and I make a {self.sound} sound.')
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    def greet(self):
        print(f'I am a {self.name} and I make a {self.sound} sound')

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    def greet(self):
        print(f'I am a {self.name} and I make a {self.sound} sound')

a = Dog('Dog', 'Woof')
b = Cat('Cat', 'Meow')
a.get_sound()
b.get_sound()