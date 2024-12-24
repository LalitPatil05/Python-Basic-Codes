class Base:
    def BaseFun(self):
        print("Base Class Method")

class Derived(Base):
    def DerivedFun(self):
        print("Derived Class Method")

class NextDerived(Derived):
    def NextDerivedFun(self):
        print("Next Derived Class Method")


obj = NextDerived()

obj.BaseFun()
obj.DerivedFun()
obj.NextDerivedFun()

