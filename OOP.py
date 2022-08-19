"""
class Dog(object):
    def __init__(self,name,age):
        print('Object Running')
        self.name = name
        self.age = age
        self.li = [1,2,3]

    def __str__(self):
        return f'object - {self.name}'

    def speak(self):
        return f"Spoken {self.name} {self.age}"

    def new_name(self,name):
        self.name = name

    def add_weight(self,weight):
        self.weight = weight

x1=Dog('Aryan',17)
print(x1)
print(x1.name)
x1.new_name('aryan')
print(x1.name)
print(x1.li)
x1.add_weight(20)
print(x1.weight)

class Cat(Dog):
    def __init__(self,name,age,cat_name):
        super().__init__(name,age)
        self.cat_name = cat_name

    def __str__(self):
        return self.cat_name

x2= Cat('Aryan',12,'Kitten')
print(x2.speak())
print(x2)
print(x2.cat_name)
x2.add_weight(12)
print(x2.weight)
x2.new_name('kitty')
print(x2.name)
"""


"""
class Vehicle():
    def __init__(self,price,gas,color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self,price,gas,color):
        super().__init__(price,gas,color)

    def beep(self):
        print('beep beep')
    
class Truck(Vehicle):
    def __init__(self,price,gas,color,tires):
        super().__init__(price,gas,color)
        self.tires = tires

    def beep(self):
        print('Honk Honk')
"""

"""
class Dog:
    dogs =[]

    def __init__(self,name):
        self.name = name
        print(self)
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print('bark!')
    
tim = Dog('Tim')
jim = Dog('Jim')
print(Dog.dogs)

class Math:
    @staticmethod
    def add(x,x2):
        return x+x2
"""