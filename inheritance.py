class Employee:

    def __init__(self,first_name,last_name,address):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.email=f"{self.first_name}"+f"{self.last_name}@company.com"
    
    def fullname(self):
        return f"{self.first_name}"+f"{self.last_name}"

emp1=Employee('Aryan','idk','GaliNo420')
print(emp1.email)


class Backup(Employee):
    def __init__(self,first_name,last_name,address,prog_lang):
        super().__init__(first_name,last_name,address)
        self.prog_lang=prog_lang

emp2=Backup('Corey','Schafer','California','Python')
print(emp2.fullname())


class BackupManager(Backup): # this inherites both Backup and Employee , here we won't need to mention Employee as Backup already inherites it 
    def __init__(self, first_name, last_name, address,prog_lang,salary):
        super().__init__(first_name, last_name, prog_lang,address)
        self.salary=salary
emp3=BackupManager('Aryan','Jain','silicion valley','C++',50000)
print(emp3.salary)