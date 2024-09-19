# Example of using higher-order functions in Python 
# Function that adds 1 to the passed value (x) 

def add(x): 
 return x + 1 

 # Function that multiplies the passed value (x) by 2 
def multiply(x): 
 return x * 2 

 # Function that applies another function on passed value (x) 
def apply(func, x): 
 return func(x)
 
result1 = apply(add, 3) # Result: 4 
result2 = apply(multiply, 3) # Result: 6 

print(result1)
print(result2)