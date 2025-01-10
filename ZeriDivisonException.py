print("Program is Starting")

try:

    a = int(input("Enter the Value of A : "))
    b = int(input("Enter the Value of B : "))

    c = a / b
    print("Divison is :",c)

except ZeroDivisionError as e:
    print(e)


print("End of Program")
    

