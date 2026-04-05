# 1. Develop a Program to undestand the control structures in Python.

# 1. If-Else Statement
print("Demonstration of If-Else Statement:")
print("Welcome to the Voting Eligibility Checker!")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  

# 2. For Loop  
print("Demonstration of For Loop:")
print("Even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)       

# 3. While Loop
print("Demonstration of While Loop:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1             

# 4. Nested If-Else
print("Demonstration of Nested If-Else:")
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:   
    print("The number is negative.")
else:    
    print("The number is zero.")

# 5. Break and Continue
print("Demonstration of Break and Continue:")
print("Numbers from 1 to 10, skipping 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)   
print("Numbers from 1 to 10, stopping at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)    

# 6. Pass Statement
print("Demonstration of Pass Statement:")
for i in range(1, 6):
    if i == 3:
        pass  # This will do nothing and continue the loop
    else:
        print(i)   