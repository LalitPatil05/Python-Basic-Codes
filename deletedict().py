# Demonstration of del keyword using also delete a dictionary in python 
# and using the specified key you can delete particular item on the dictionary...

dict = {
    "brand":"Ford",
    "model":"mustang",
    "year":1965
}

print(dict)

del dict["brand"]

print(dict)

del dict

print(dict)