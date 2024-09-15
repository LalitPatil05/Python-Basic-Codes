# Demonstratio of Variable Length Arguments in Python..

def MyFun(*t): # Define the tuple
    print("Type of Value to be Passed : ",type(t))
    print("Elements are to be Passed : ")
    for x in t:
        print(x)

MyFun(1,2,3,4,5,6,7,8,9,0) # Function Calling