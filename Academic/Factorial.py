# Write a Program to Calculate the Factorial of Given Number.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result 

number = int(input("Enter a number to calculate its factorial: "))
fact = factorial(number)
print(f"The Factorial of {number} is: {fact}")  