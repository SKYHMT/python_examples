class Mandy:
    def move(self):
        print("move")

    def plus(a,b):
        print(a^2+b^2)

    def __init__(self, x, y):
       self.x = x
       self.y = y


# mandy1 = Mandy()
# mandy1.move()
mandy = Mandy (30, 20)
print(mandy.x)

# exercise:
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


mandy = Person("Mandy HE")
print(mandy.name)
mandy.talk()

