class Base1:
    def Base1Fun(self):
        print("Base 1 Method")

class Base2:
    def Base2Fun(self):
        print("Base 2 Method")

class Derived(Base1,Base2):
    def DerivedMethod(self):
        print("Derived Method")


obj = Derived()
obj.Base1Fun()
obj.Base2Fun()
obj.DerivedMethod()
