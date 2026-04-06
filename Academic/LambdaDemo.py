# Write a Program to calculate the area of triangle using lambda function.


area_of_triangle = lambda base, height: 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = area_of_triangle(base, height)
print("The area of the triangle is:", area) 
