# Write a Program to Print Fibonacci Series up to n terms.

n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:    
    print("Fibonacci sequence up to", n, "terms:")
    while a < n:
        print(a, end=' ')
        a, b = b, a + b 
        print("Updated values: a =", a, "b =", b)
        count += 1 
