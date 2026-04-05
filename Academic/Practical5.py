# Developing Programs for data structures algortithms using Python - Searching, Sorting and hash tables.

# 1. Searching Algorithms

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if target is not found

print("Demonstration of Linear Search:")
my_list = [5, 3, 2, 8, 1]
target = 2
result = linear_search(my_list, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
print("------------------------------------------------------------")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if target is not found  

print("Demonstration of Binary Search:")
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(sorted_list, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:    print(f"Element {target} not found in the list.")

print("------------------------------------------------------------")   

# 2. Sorting Algorithms 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr

print("Demonstration of Bubble Sort:")
unsorted_list = [64, 34, 25, 12, 22,    11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)
print("------------------------------------------------------------")   

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr  

print("Demonstration of Selection Sort:")
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)     
print("Sorted list:", sorted_list)
print("------------------------------------------------------------")       

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print("Demonstration of Insertion Sort:")
unsorted_list = [12, 11, 13, 5, 6]  
sorted_list = insertion_sort(unsorted_list)
print("Sorted list:", sorted_list)
print("------------------------------------------------------------")

# 3. Hash Tables

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, None)

    def delete(self, key):
        if key in self.table:
            del self.table[key] 

print("Demonstration of Hash Table:")

hash_table = HashTable()        
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print("Search for 'name':", hash_table.search("name"))
print("Search for 'age':", hash_table.search("age"))
hash_table.delete("name")
print("Search for 'name' after deletion:", hash_table.search("name")) 
      
print("------------------------------------------------------------")
