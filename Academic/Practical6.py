# Develop Program to learn Regular Expressions Using Python.

import re

# 1. Validating Email Addresses
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid email address."
    else:
        return "Invalid email address."

print("Demonstration of Validating Email Addresses:")
email = input("Enter an email address: ")
print(validate_email(email))
print("------------------------------------------------------------")   

# 2. Extracting Phone Numbers
def extract_phone_numbers(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

print("Demonstration of Extracting Phone Numbers:")
text = "Contact us at 123-456-7890 or 987.654.3210."
phone_numbers = extract_phone_numbers(text)     
print("Extracted phone numbers:", phone_numbers)
print("------------------------------------------------------------")  

# 3. Replacing Substrings
def replace_substring(text, old, new):
    pattern = re.escape(old)
    return re.sub(pattern, new, text)

print("Demonstration of Replacing Substrings:")
text = "The quick brown fox jumps over the lazy dog."
old_substring = "fox"
new_substring = "cat"
modified_text = replace_substring(text, old_substring, new_substring)
print("Modified text:", modified_text)
print("------------------------------------------------------------")

# 4. Splitting Strings
def split_string(text, delimiter):
    pattern = re.escape(delimiter)
    return re.split(pattern, text)

print("Demonstration of Splitting Strings:")
text = "apple,banana,cherry,grape"
delimiter = ","
fruits = split_string(text, delimiter)
print("Split fruits:", fruits)      
print("------------------------------------------------------------")

# 5. Finding All Occurrences
def find_all_occurrences(text, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    return re.findall(pattern, text)

print("Demonstration of Finding All Occurrences:")
text = "The rain in Spain stays mainly in the plain."
word = "in"
occurrences = find_all_occurrences(text, word)
print(f"Occurrences of '{word}':", occurrences) 
print("------------------------------------------------------------")

