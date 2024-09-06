a=0
b =1

n = int(input("Enter the Range of Fibonacci Series : "))

while a < n:
    print(a)
    #a, b = b, a+b
    a=b
    b=a+b