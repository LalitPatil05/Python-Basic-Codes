# Demonstration of pop() method in python 
# to removal the items in the dictionary using specified key...

dict = {
    "brand" : "ford",
    "model" : "Mustang",
    "Year" :  1964
}

print(dict)

dict.pop("model")

print(dict)

dict.popitem()

print(dict)