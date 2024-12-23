class Calculator:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b


    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

obj = Calculator()

a = obj.add(4,2)
b = obj.sub(6,2)
c = obj.mul(4,2)
d = obj.div(4,2)

print("Addition is :",a)
print("Substraction is : ",b)
print("Multiplication is :",c)
print("Divison is : ",d)
