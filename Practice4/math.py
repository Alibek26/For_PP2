#Exercise 1
import math
degree = float(input("Input degree: ")) #15

radian = math.radians(degree) 
print(f"Output radian: {radian:.6f}") #Output radian: 0.261799

#Exercise 2
height = float(input("Height: ")) # 5
base1 = float(input("Base, first value: ")) # 5
base2 = float(input("Base, second value: ")) # 6

area = (base1 + base2) * height / 2
print(f"Expected Output: {area}") # Expected Output: 27.5

#Exercise 3
import math

n = int(input("Input number of sides: ")) # 4
a = float(input("Input the length of a side: ")) # 25

area = (n * a**2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area}") # The area of the polygon is: 625.0

#Exercise 4
base = float(input("Length of base: ")) # 5
height = float(input("Height of parallelogram: ")) # 6

area = base * height

print(f"Expected Output: {area}") # Expected Output: 30.0