# 2. Develop a Program to learn different types of structures (list, dictonary, tuple, set) in Python.

# 1. List
fruits = ["apple", "banana", "cherry"] 
print("Fruits List:", fruits)

# append
fruits.append("orange")
print("Updated Fruits List:", fruits)

# copy
fruit_copy = fruits.copy()
print("Copy of Fruits List:", fruit_copy)   

#count
print("Count of 'banana' in Fruits List:", fruits.count("banana"))

# extend
more_fruits = ["grape", "melon"]
fruits.extend(more_fruits)
print("Extended Fruits List:", fruits)  

# index
print("Index of 'cherry' in Fruits List:", fruits.index("cherry"))  

# insert 
fruits.insert(1, "kiwi")
print("Fruits List after inserting 'kiwi' at index 1:", fruits)

# pop
popped_fruit = fruits.pop(2)
print("Popped Fruit:", popped_fruit)
print("Fruits List after popping:", fruits)

# remove   
fruits.remove("cherry")
print("Fruits List after removing 'cherry':", fruits)

# reverse
fruits.reverse()
print("Reversed Fruits List:", fruits)

# sort
fruits.sort()
print("Sorted Fruits List:", fruits)

print("------------------------------------------------------------")


# 2. Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Person Dictionary:", person)
person["age"] = 31
print("Updated Person Dictionary:", person) 


# getitem
print("Person's name:", person["name"])

# iter 
for key in person:
    print(f"{key}: {person[key]}")  

# copy
person_copy = person.copy()
print("Copy of Person Dictionary:", person_copy)

# items
print("Person Dictionary Items:", person.items())

# keys
print("Person Dictionary Keys:", person.keys())

# values
print("Person Dictionary Values:", person.values())

# fromkeys
keys = ["name", "age", "city"]
default_value = "Unknown"
new_person = dict.fromkeys(keys, default_value)
print("New Person Dictionary from keys:", new_person)

# pop
popped_value = person.pop("city")
print("Popped Value:", popped_value)
print("Person Dictionary after popping 'city':", person)

# popitem
popped_item = person.popitem()
print("Popped Item:", popped_item)
print("Person Dictionary after popping an item:", person)

# update
person.update({"name": "Bob", "age": 25})
print("Person Dictionary after update:", person)

print("------------------------------------------------------------")

# 3. Tuple
coordinates = (10, 20)
print("Coordinates Tuple:", coordinates)
# Tuples are immutable, so we cannot change their values
# coordinates[0] = 15  # This will raise an error   

# sizeof 
import sys
print("Size of Fruits List:", sys.getsizeof(fruits), "bytes")
print("Size of Person Dictionary:", sys.getsizeof(person), "bytes")
print("Size of Coordinates Tuple:", sys.getsizeof(coordinates), "bytes")    

# count
print("Count of 'apple' in Fruits List:", fruits.count("apple"))    

# index 
print("Index of 'melon' in Fruits List:", fruits.index("melon"))

# getitem
print("First fruit in the list:", fruits[0])

print("------------------------------------------------------------")

# 4. Set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers Set:", unique_numbers)
unique_numbers.add(6)
print("Updated Unique Numbers Set:", unique_numbers)
unique_numbers.add(3)  # Adding a duplicate value will not change the set
print("Unique Numbers Set after adding duplicate:", unique_numbers)


# union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("Union of Set A and Set B:", union_set)

# intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B:", intersection_set)

# difference
difference_set = set_a.difference(set_b)
print("Difference of Set A and Set B:", difference_set)

# symmetric_difference
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of Set A and Set B:", sym_diff_set) 

# pop 
popped_element = unique_numbers.pop()
print("Popped Element from Unique Numbers Set:", popped_element)
print("Unique Numbers Set after popping an element:", unique_numbers)

# remove
unique_numbers.remove(2)
print("Unique Numbers Set after removing 2:", unique_numbers)

# discard
unique_numbers.discard(10)  # Discarding a non-existent element will not raise
print("Unique Numbers Set after discarding 10:", unique_numbers)
