# Наследование
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
pass

#Задача

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start_engine(self):
        pass
        

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        Vehicle.__init__(self, brand, model, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        return f"Двигатель запущен {self.brand} {self.model} {self.year} с {self.num_doors} дверми"
    
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        Vehicle.__init__(self, brand, model, year)
        self.has_sidecar = has_sidecar
    
    def start_engine(self):
        if self.has_sidecar == 1:
            return f"Двигатель запущен {self.brand} {self.model} {self.year} с подвисной коляской"
        if self.has_sidecar == 0:
            return f"Двигатель запущен {self.brand} {self.model} {self.year} без подвисной коляски"
        

car = Car('BMV', 'M5', '2025', 4)
motocycle = Motorcycle('Suzuki', 'M5', '2025', 1)
print(car.start_engine())
print(motocycle.start_engine())