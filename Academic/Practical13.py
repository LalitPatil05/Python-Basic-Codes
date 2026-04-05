# Demonstrate use of DataFrame method and use of .csv File.

import pandas as pd

# Create a DataFrame from a .csv file.
df = pd.read_csv('data.csv')      
print(df)

# Display the DataFrame sorted by the 'Age' column.
print(df.sort_values('Age'))
# by the 'Name' column.
print(df.sort_values('Name'))  

# by the 'Age' column in descending order.
print(df.sort_values('Age', ascending=False))   
# by the 'Name' column in descending order.
print(df.sort_values('Name', ascending=False)) 

# by the 'Age' column and then by the 'Name' column.
print(df.sort_values(['Age', 'Name']))
# by the 'Age' column in descending order and then by the 'Name' column in descending order.
print(df.sort_values(['Age', 'Name'], ascending=[False, False]))    

