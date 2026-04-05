# Write a Program to Check that Given Number is Armstrong Number or Not.

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str) # Comprehension
    return armstrong_sum == num

try:
    number = int(input("Enter a number: "))

    if is_armstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")    

except ValueError:
    print("Invalid input. Please enter a valid integer.")   

