# Function
def greet(name):
    print("Hello", name)

greet("Lalit")

# Recursion (Factorial)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print("Factorial:", fact(5))

# Mutability
lst = [1, 2, 3]
lst[0] = 100
print(lst)
