class Demo:
    def add(self,a,b):
        print("Sum is : ",a+b)

class Demo2(Demo):
    def add(self,a,b,c):
        print("Sum is : ",a+b+c)

obj1 = Demo()
obj1.add(2,4)

print("-----------------------------")

obj2 = Demo2()
obj2.add(3,4,6)
