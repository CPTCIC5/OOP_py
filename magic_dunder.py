class Work():

    def fullname(self):
        return f"{self.name}"+f"{self.last_name}"

    def __str__(self):  #defines a proper name for objects  in a  function
        return self.name

    def __repr__(self):    #defines a proper name for objects  in a  function
        return self.name

    def __len__(self):  # used to calcuate len of str and datatypes and later can be displayed below
        return len(self.fullname())

    def __init__(self, name,last_name, address, number,is_done):
        self.name=name
        self.last_name=last_name
        self.address=address
        self.number=number
        self.is_done=is_done

user2=Work('Aryan','Noob','Nahiptavai',96969,False)
print(user2)
print(len(user2)) # without the __len__ func it will not work
