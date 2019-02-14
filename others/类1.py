class Cat:

    def __init__(self, name):
        print("------初始化----")
        self.name = name

    def eat(self):
        print("猫吃鱼")

    def __del__(self):
        print("tom gone")

    def __str__(self):
        return "i am a cat"
    


tom = Cat("Tom")
tom.eat()
print(tom.name)

print(tom)
