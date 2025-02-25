class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says gav"
    
my_cat = Cat('Cat')
my_dog = Dog('Dog')
print(my_dog.speak())
print(my_cat.speak())