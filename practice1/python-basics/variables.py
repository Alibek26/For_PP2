#Creating Variables!!!

#Example 1
x = 5
y = "John"
print(x)
print(y)

#Example 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Variable Names !!!

#Example 1 Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example 2 Illegal variable names:
""" 
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Assign Multiple Values!!!

#Example 1 Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Example 2 One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Example 3 Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables!!!

#Example 1
x = "Python is awesome"
print(x)

#Example 2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Example 3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example 4
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
#Example
""" 
x = 5
y = "John"
print(x + y)
"""

#Example 5
x = 5
y = "John"
print(x, y)

#Global Variables!!!

#Example 1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example 2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
#Example 1
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example 2
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)