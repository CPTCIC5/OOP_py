"""
class Fruit:
    pass

apple = Fruit()
banana = Fruit()

apple.color = 'red'
apple.size = 23

banana.color  = 'pink'
print(banana.size)
"""


class Fruit:
    total_fruits = 20
    def __init__(self,name,color="white"):
        self.name = name
        self.color = color

    @classmethod
    def total_fruits(cls):
        return cls.total_fruits

    @staticmethod
    def square(n):
        return n*n

    def info(self):
        return f"myself {self.name} i'm a fruit my color is {self.color}"
    def __str__(self):
        return self.name

apple = Fruit("Apple")
banana = Fruit("Banana","Blue")

print(apple.info())
print(Fruit.square(5))