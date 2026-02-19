##The __init__() Method!!!
"""
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
"""
#Example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#Why Use __init__()?!!!
#Without the __init__() method, you would need to set properties manually for each object:
#Example 
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)
#Using __init__() makes it easier to create objects with initial values:
#Example 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

#Default Values in __init__()!!!
#You can also set default values for parameters in the __init__() method:
#Example
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)