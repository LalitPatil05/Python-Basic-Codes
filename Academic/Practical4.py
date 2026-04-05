# Develop a Program to Understand the Object Oriented Programming Using Python.

# 1. Class and Object

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")


print("Demonstration of Class and Object:")

my_car = Car("Toyota", "Fortuner", 2020)
my_car.display_info()    

print("------------------------------------------------------------")

# 2. Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_battery_info(self):
        print(f"Battery Size: {self.battery_size} kWh") 

print("Demonstration of Inheritance:")

my_electric_car = ElectricCar("Tesla", "Model 3", 2021, 75)
my_electric_car.display_info()
my_electric_car.display_battery_info()  

print("------------------------------------------------------------")   

# 3. Polymorphism

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"  

class Cat(Animal):
    def speak(self):
        return "Meow!"  

print("Demonstration of Polymorphism:")
animals = [Dog(), Cat()]
for animal in animals:  
    print(animal.speak())

print("------------------------------------------------------------")  

# 4. Encapsulation

class BankAccount:  
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

print("Demonstration of Encapsulation:")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
# Trying to access the private attribute directly will raise an error
# print(account.__balance)  # This will raise an error because __balance is private 