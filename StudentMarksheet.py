java = int(input("Enter the java subject marks : "))
python = int(input("Enter the python subject marks :"))
math = int(input("Enter the maths subject marks : "))
english  = int(input("Enter the english subject marks : "))
science = int(input("Enter the science subject marks : "))

totalmarks = java + python + math + english + science

print("Total Marks is : ",totalmarks)

percentage = (totalmarks/500)*100

print("Percentage is : ",percentage)

if(percentage<50):
    print("C Grade..!!")
elif(percentage<80):
    print("B Grade..!!")
elif(percentage>90):
    print("A Grade..!!")


