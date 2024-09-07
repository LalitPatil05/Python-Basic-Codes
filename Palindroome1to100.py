l1=[] # create a empty list for store the 1 t0 100 prime numbers

for x in range(1,100):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x,end=' ')
        l1.append(x) # append elemnt into the list

print("\n")
print("List is :")
print(l1)

length = len(l1) # calculate the length of list
print("Length of list is : ",length)


mid = length//2 # find the mid of the list

result = (l1[mid]+l1[mid-1])
print("Sum of Mid range numbers is : ",result)