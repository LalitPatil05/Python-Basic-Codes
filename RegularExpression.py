import re

text = "My number is 9876543210"
pattern = r"\d+"

result = re.findall(pattern, text)
print(result)
