class MyError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age > 18  and age < 100:
        print("Congratulation, you are eligible")
    else:
        raise MyError('Sorry, you are not Eligible')
except MyError as e:
    print(e)
