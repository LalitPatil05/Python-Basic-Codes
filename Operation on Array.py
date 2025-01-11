arr = ["Maruti", "SuzUki", "Honda",]

print(type(arr))

print("Before Appendin Elements Array is :")
for x in arr:
    print(x)


print("After Appending Elements Array is ")
arr.append("Toyota")
arr.append("BMW")


for y in arr:
    print(y)


arr.pop()


print("After Deleting array is :")
print(arr)
    
