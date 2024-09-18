Current_Balance = 10000

Withdraw_Amount = 1500

try:
    if(Withdraw_Amount > Current_Balance):
        print("Insuffecient Balance..!!")
    else:
        Current_Balance = Current_Balance - Withdraw_Amount
        print("Withdraw Amount is : ",Withdraw_Amount)
        print("Current Balance is : ",Current_Balance)
        
except ValueError:
    print("Invalid Transaction..!!")

print("End of Statement")
    
