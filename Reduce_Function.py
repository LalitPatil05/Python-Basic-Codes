import functools

l = [1,2,3,4]

product = functools.reduce(lambda  x,y : x * y, l)

print("Product of List is : ",product)


s = functools.reduce(lambda x,y : x+y, l)

print("Sum of List is : ",s)
