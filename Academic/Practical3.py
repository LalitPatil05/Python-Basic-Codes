# Develop a program to learn concept of functions scoping, recursion and list mutability in Python.

# 1. Function Scoping

def outer_function():
    outer_var = "I am an outer variable."

    def inner_function():
        inner_var = "I am an inner variable."
        print(outer_var)  # Accessing outer variable
        print(inner_var)  # Accessing inner variable

    inner_function()
    # print(inner_var)  # This will raise an error because inner_var is not accessible here

print("Demonstration of Function Scoping:")
outer_function()
print("------------------------------------------------------------")

# 2. Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
print("Demonstration of Recursion:")
number = 5
print(f"Factorial of {number} is {factorial(number)}")
print("------------------------------------------------------------")       

# 3. List Mutability
fruits = ["apple", "banana", "cherry"]
print("Original Fruits List:", fruits)
fruits[1] = "blueberry"  # Modifying the list
print("Modified Fruits List:", fruits)
fruits.append("orange")  # Adding an element to the list
print("Fruits List after appending 'orange':", fruits)

print("------------------------------------------------------------")
# Demonstrating that lists are mutable
def modify_list(lst):
    lst.append("new item")
      
my_list = ["item1", "item2"]
print("Original List:", my_list)
modify_list(my_list)
print("Modified List after function call:", my_list)

