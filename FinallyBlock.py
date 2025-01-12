print("Program is Starting...!!!")

try:
    a = int(input("Enter the Value of a :"))
    b = int(input("Enter the Value of b :"))

    c = a / b
    print("Divison is : ",c)

except ZeroDivisionError as e:
    print(e)
    
finally:
    print("Finally Block")


print("Program is END..!!")
    
