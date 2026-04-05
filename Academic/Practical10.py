# Demonstrate Implementation functional Programming tools such as filter, map, reduce, lambda functions, and list comprehensions.

# 1. Using filter to filter out odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers using filter and lambda:", odd_numbers)
print("------------------------------------------------------------")   

# 2. Using map to convert a list of temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print("Temperatures in Fahrenheit using map and lambda:", fahrenheit)
print("------------------------------------------------------------")

# 3. Using reduce to calculate the factorial of a number
from functools import reduce
def factorial(n):   
    if n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))
number = 5
result = factorial(number)
print(f"Factorial of {number} using reduce and lambda:", result)
print("------------------------------------------------------------")

# 4. Using list comprehensions to create a list of squares of numbers from 1 to 10      
squares = [x ** 2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10 using list comprehensions:", squares)
print("------------------------------------------------------------")

# 5. Using list comprehensions to filter and create a list of even numbers from a list
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers using list comprehensions:", even_numbers)      
print("------------------------------------------------------------")