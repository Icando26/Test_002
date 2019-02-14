class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.listItem = []

        print("初始化")

    def __str__(self):
        return "我的名字是%s,体重是%2f" % (self.name, self.weight)

    def addItem(self, name):
        self.listItem.append(name)
        print("-------")


Jack = Person("jack", 12)

print(Jack.__str__())
