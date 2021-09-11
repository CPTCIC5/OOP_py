class Employee():

    raise_amount=1.04
    no_of_employees=0

    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email=first_name + '.' +last_name + '@gmail.com'

        Employee.no_of_employees +=1
    
    def fullname(self):
        return str(f'{self.first_name}{self.last_name}')
    
    def apply_raise(self):
        self.pay=int(self.pay + self.raise_amount)

emp=Employee('Aryan','Jain',50000)
emp2=Employee('Corey','Schafer',99999)

#print(emp.raise_amount)
#print(Employee.raise_amount)
#print(emp2.raise_amount)

#print(emp.pay)

'''
print(emp2.no_of_employees)
print(emp.no_of_employees)
print(Employee.no_of_employees)
'''


