class Cat:
    def eat(self):
        print("猫吃鱼")

    def run(self):
        print("%s 猫跑了" % self.name)


tom = Cat()
tom.eat()
addr = id(tom)

print("%x ==十六进制=" % addr)
tom = Cat()
tom.name = "Tom"
tom.run()
addr = id(tom)
"重新分配地址了"
print("%s   +++" % addr)
print("%d   ---" % addr)
print("%x ==十六进制=" % addr)
