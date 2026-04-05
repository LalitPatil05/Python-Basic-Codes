# Demonstrate the Concept of String-Based Exceptions, Class-Based Exceptions and Nesting Exception Handleers.

# 1. String-Based Exceptions    
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except "ZeroDivisionError": 
    print("Error: Cannot divide by zero.")
except "ValueError":    
    print("Error: Invalid input. Please enter numbers.")    

print("------------------------------------------------------------")

# 2. Class-Based Exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")        

print("------------------------------------------------------------")

# 3. Nesting Exception Handlers
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")        

