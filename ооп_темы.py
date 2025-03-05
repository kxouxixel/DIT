# # Наследование
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         pass
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says meow"
    
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says gav"
    
# my_cat = Cat('Cat')
# my_dog = Dog('Dog')
# print(my_dog.speak())
# print(my_cat.speak())
# pass

# #Задача

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
        
#     def start_engine(self):
#         pass
        

# class Car(Vehicle):
#     def __init__(self, brand, model, year, num_doors):
#         Vehicle.__init__(self, brand, model, year)
#         self.num_doors = num_doors
    
#     def start_engine(self):
#         return f"Двигатель запущен {self.brand} {self.model} {self.year} с {self.num_doors} дверми"
    
    
# class Motorcycle(Vehicle):
#     def __init__(self, brand, model, year, has_sidecar):
#         Vehicle.__init__(self, brand, model, year)
#         self.has_sidecar = has_sidecar
    
#     def start_engine(self):
#         if self.has_sidecar == 1:
#             return f"Двигатель запущен {self.brand} {self.model} {self.year} с подвисной коляской"
#         if self.has_sidecar == 0:
#             return f"Двигатель запущен {self.brand} {self.model} {self.year} без подвисной коляски"
        

# car = Car('BMV', 'M5', '2025', 4)
# motocycle = Motorcycle('Suzuki', 'M5', '2025', 1)
# print(car.start_engine())
# print(motocycle.start_engine())

# # Полиморфизм

# class Bird:
#     def speak(self):
#         return "Tweet"
    
# class Dog:
#     def speak(self):
#         return "Woof"

# class Cat:
#     def speak(self):
#         return "Meow"
    
# def make_sound(animal):
#     print(animal.speek())
    

# sparrow = Bird()
# bulldog = Dog()
# sphinks = Cat()

# make_sound(sparrow)
# make_sound(bulldog)

# # Доп.контент

# animals = [Dog(), Cat(), Bird()]

# # Инкапсуляция

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return True
#         return False
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return True
#         return False
        
        
#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(200)
# account.deposit(100)
# print(account.get_balance())
# account.withdraw(50)
# print(account.get_balance())
# # print(account.__balance)         <== ощибка(я кобы нет)

# # Задача (+)

# class Rectangle:
#     def __init__(self, w, h):
#         self.__w = w
#         self.__h = h
        
#     def s_math(self):
#         return f"{self.__w * self.__h}"
    
#     def p_math(self):
#         return f"{self.__w + self.__h + self.__w + self.__h}"
    
# Rect1 = Rectangle(3, 8)
# print(Rect1.s_math())
# print(Rect1.p_math())

# # 2-ой урок классов ооп

# # Задача на флекс :)))

# import pygame as pg
# import random

# W, H, FPS = 600, 600, 120
# pg.init()
# win = pg.display.set_mode((W, H))

# def load_img(name):
#     img = pg.image.load(name)
#     img = img.convert()
#     colorkey = img.get_at((0, 0))
#     img.set_colorkey(colorkey)
#     return img

# class Inginirium(pg.sprite.Sprite):
    
#     def __init__(self, *group):
#         super().__init__(*group)
#         self.image = load_img('sonic2.png')
#         self.image = pg.transform.scale(self.image, (100, 100))
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(W)
#         self.rect.y = random.randrange(H)
       
#     def update(self):
#         self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        
# all_sprites = pg.sprite.Group()
    
# for i in range(50):
#     Inginirium(all_sprites)
        
        
# while True:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             exit()
        
#     all_sprites.update()
#     win.fill((255, 255, 255))
#     all_sprites.draw(win)
#     pg.display.update().  