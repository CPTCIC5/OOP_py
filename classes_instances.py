
'''
class Employee():
    pass

emp=Employee()
emp2=Employee()

print(emp,emp2)

emp.first_name='Aryan'
emp.last_name='Jain'


emp2.first_name='Corey'
emp2.last_name='Schafer'

print(emp2.last.name)'''




'''
class Employee():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

emp=Employee('Aryan','Jain')
emp2=Employee('Corey','Schafer')

print(emp2.last_name)'''



class Employee():
    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email=first_name + '.' +last_name + '@gmail.com'
    
    def fullname(self):
        return str(f'{self.first_name}{self.last_name}')


emp=Employee('Aryan','Jain',50000)
emp2=Employee('Corey','Schafer',99999)

print(emp2.fullname())