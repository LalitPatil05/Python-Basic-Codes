# Write a Program to Demonstrate Inheritance in Python.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Cat meows"  

# Creating instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")  
cat = Cat("Whiskers", "Black")  

# Demonstrating inheritance and method overriding
print(f"{dog.name} is a {dog.breed} and says: {dog.speak()}")
print(f"{cat.name} is a {cat.color} cat and says: {cat.speak()}")   

