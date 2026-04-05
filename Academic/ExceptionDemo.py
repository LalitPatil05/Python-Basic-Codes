# Write a Program to Demonstrate the Exception Handling in Python.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please provide a non-zero divisor.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers for division.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 

# Taking user input for numbers to divide
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    divide_numbers(number1, number2)
except ValueError:
    print("Error: Invalid input. Please enter numeric values.") 
