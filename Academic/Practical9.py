# Demonstrate implementation of the Anonymous Functions Lambda.

# 1. Using lambda to create a simple function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print("Result of adding 5 and 3 using lambda:", result)
print("------------------------------------------------------------")   

# 2. Using lambda with the map function to square a list of numbers 
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using lambda and map:", squared_numbers)
print("------------------------------------------------------------")   

# 3. Using lambda with the filter function to filter out even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda and filter:", even_numbers)
print("------------------------------------------------------------")

# 4. Using lambda with the sorted function to sort a list of tuples based on the second element
tuples_list = [(1, 'grapes'), (2, 'apple'), (3, 'banana')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print("Sorted tuples based on the second element using lambda:", sorted_tuples)
print("------------------------------------------------------------")   

# 5. Using lambda with the reduce function to calculate the product of a list of numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers using lambda and reduce:", product)       
