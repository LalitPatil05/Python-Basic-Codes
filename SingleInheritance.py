class Base:
    def BaseFun(self):
        print("Base Class Method")



class Derived(Base):
    def DerivedFun(self):
        print("Derived Class Method")


obj = Derived()


obj.BaseFun()
obj.DerivedFun()



    
