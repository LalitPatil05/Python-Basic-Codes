l = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x : x%2==0,l))
odd = list(filter(lambda x  : x%2!=0,l))

print("Even List is : ",even)
print("Odd List is : ",odd)

