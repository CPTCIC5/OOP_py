#property deco are used for functions inside  a class so we can call them directly as a instance not by () example-fullname() to emp2.fullname

class Employee:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    @property
    def email(self): #we can make a instance self.email=self.first_name+self.last_name but we aren't cez
        return f"{self.first_name}.{self.last_name}@gmail.com"


emp1=Employee('Aryan','Jain')
print(emp1.email)