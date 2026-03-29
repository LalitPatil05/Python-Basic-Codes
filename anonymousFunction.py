from functools import reduce

lst = [1, 2, 3, 4, 5]

# Filter (even numbers)
even = list(filter(lambda x: x % 2 == 0, lst))
print(even)

# Reduce (sum)
total = reduce(lambda x, y: x + y, lst)
print(total)
