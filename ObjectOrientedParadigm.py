class Student:
    def __init__(self, name, marks): # constructor
        self.name = name
        self.marks = marks

    def display(self): # method
        print(self.name, self.marks)

s1 = Student("Lalit", 90)
s1.display()
