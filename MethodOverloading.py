class MethodOverloading:
    def Add(self,name=None):
        if name is not None:
           print("Hello"+self.name)
        else:
            print("Hello")


obj = MethodOverloading
obj.Add("Vikas")
