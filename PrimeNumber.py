p = int(input("Enter the Starting Range : "))
q = int(input("Enter the Ending Range : "))

numlist = []

for x in range(p,q):
        for i in range(2,x):
            if x%i==0:
                break
        else:
             print(x,end=',')
             numlist.append(x)
                    
print()
print("List of Prime Numbers is : ")
print(numlist)
     
