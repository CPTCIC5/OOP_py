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

"""
class Employee:
    raise_amount=1.04

    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        
    @property
    def email(self):
        return self.fname+self.lname+'@hotmail.com'

    def fullname(self):
        return self.fname+self.lname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date=datetime.date()
print(Employee.is_workday(my_date))

emp1=Employee('Aryan','Noob',100)
emp2=Employee('Ishan','Sharma',1000000)
print(emp1.raise_amount)
emp1.set_raise_amt(1.05)
print(emp1.raise_amount)

class Developer(Employee):
    
        super().__init__(fname,lname,pay)
        self.stack=stack

emp3=Developer('Aryan','Noob',5000,'Django+React')
print(emp3.pay)
emp3.apply_raise()
print(emp3.pay)
print(emp3.stack)
#print(emp1.stack)
"""

"""
class Employee:
    raise_amount=1.04

    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
    
    def __str__(self):
        return self.fname

    @property
    def email(self):
        return f"{self.fname}-{self.lname}@gmail.com"

    def fullname(self):
        return f"{self.fname}-{self.lname}"

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    
    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Manager(Employee):
    def __init__(self, fname, lname, pay,branch):
        super().__init__(fname, lname, pay)
        self.branch=branch
"""


"""
class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        return ('Hi im ',self.name)

    def change_age(self,age):
        self.age=age

    def add_weight(self,weight):
        self.weight=weight

dog1=Dog('Aryan',5)
dog1.speak()
print(dog1.age)
dog1.change_age(6)
print(dog1.age)

dog1.add_weight(20)
print(dog1.weight)

class Cat(Dog):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color=color

    def speak(self):
        return self.name

x1=Cat('Aryan',11,'Block')
print(x1.speak())

"""