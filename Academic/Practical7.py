# Demonstrate the Concept of exception handling using try/except/else statemetnt, unified try/except statement, and finally statement, raise statement, assert statement, catch multiple specific expresssion.

# 1. Using try/except/else statement

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")

print("------------------------------------------------------------")

# 2. Using unified try/except statement

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")
print("------------------------------------------------------------")

# 3. Using finally statement

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")
finally:
    print("This block will always execute, regardless of exceptions.")
print("------------------------------------------------------------")

# 4. Using raise statement

def calculate_square_root(num):
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return num ** 0.5
try:
    number = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(number)
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"The square root of {number} is: {result}")

# calculate_square_root(-4)  # This will raise an exception
calculate_square_root(16)  # This will return 4.0
print("------------------------------------------------------------")

# 5. Using assert statement

def divide_numbers(num1, num2):
    assert num2 != 0, "Cannot divide by zero."
    return num1 / num2
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = divide_numbers(number1, number2)
except AssertionError as e:
    print(f"Assertion Error: {e}")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
else:
    print(f"The result of {number1} divided by {number2} is: {result}")

#divide_numbers(10, 0)  # This will raise an assertion error
divide_numbers(10, 2)  # This will return 5.0
print("------------------------------------------------------------")

# 6. Catching multiple specific exceptions

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")
