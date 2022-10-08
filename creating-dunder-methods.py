class Person():
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return self.name
    
    def __mul__(self,x):
        if type(x) != int or type(x) != float:
            raise Exception('Invalid arguments')
        self.name = self.name * x

    def __call__(self,y):
        print('made this calling function')

    def __len__(self):
        return len(self.name)
p=Person('tim')
p(4)