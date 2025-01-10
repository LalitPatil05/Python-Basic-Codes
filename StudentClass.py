class Student:

    
    def GetData(self):
        self.rollno=int(input("Enter the Student Roll No : "))
        self.Name=input("Enter the Student Name : ")
        self.Marks=float(input("Enter the Student Marks : "))

    def Display(self):
        print("Student Roll No. is : ",self.rollno)
        print("Student Name is : ",self.Name)
        print("Student Marks is : ",self.Marks)


s = Student()

s.GetData()
s.Display()
