# Function Decleration
def Sum(n):
    s=0
    for x in range(n+1):
        s = s + x
    return s

# Driver Code
Result = Sum(5) # Function Callig
print("Sum is : ",Result)