class A:
    def FunA(self):
        print("I am Class A Method")

class B:
    def FunB(self):
        print("I am Class B Method")

class C(A,B):
    def FunC(self):
        print("I am Class C Method")


obj = C()

obj.FunC()
obj.FunB()
obj.FunA()
