# Demonstration of Module Creation, Module Usage.

# Module Usage   

import math_module 

print("Demonstration of Module Usage:")
name = input("Enter your name: ")
greeting = math_module.greet(name)      
print(greeting)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"{num1} + {num2} = {math_module.add(num1,num2)}")
print(f"{num1} - {num2} = {math_module.subtract(num1, num2)}")
print(f"{num1} * {num2} = {math_module.multiply(num1, num2)}")

try:    
    print(f"{num1} / {num2} = {math_module.divide(num1, num2)}")
except ValueError as e:
    print(f"Error: {e}")    

