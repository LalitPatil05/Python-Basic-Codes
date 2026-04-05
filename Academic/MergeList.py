# Write a Program to Merge the Two Lists and clear the elements of second list.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]    

print("List 1: ", list1)
print("List 2: ", list2)

# Merging the two lists
merged_list = list1 + list2
print("Merged List: ", merged_list) 

# Clearing the elements of second list
list2.clear()
print("List 2 after clearing: ", list2)     
