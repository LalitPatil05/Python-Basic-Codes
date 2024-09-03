# demonstration of copy() method in dictionary..
# usind it we can copy the content of old dictionary into the new dictionary..

dict = {
    "id":101,
    "name":"Lalit",
    "fees":1000
}

print(dict)

newdict = dict.copy()

print(newdict)
print(dict)