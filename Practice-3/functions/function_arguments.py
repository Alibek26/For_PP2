#Arguments!!!
#A "parameter" is the variable listed inside the parentheses in the function definition.
#An "argument" is the actual value that is sent to the function when it is called.
#Example 1
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Example 2
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#Example 3
#This function expects 2 arguments, and gets 2 arguments::
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Default Parameter Values!!!
#You can assign default values to parameters. If the function is called without an argument, it uses the default value:
#Example 1
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Example 2
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Keyword Arguments!!!
#You can send arguments with the key = value syntax.
#Example 1
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Examle 2
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

#Positional Arguments!!!
#When you call a function with arguments without using keywords, they are called positional arguments.
#Example 1
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#Example 2
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

#Mixing Positional and Keyword Arguments!!!
#You can mix positional and keyword arguments in a function call.
#Example 1
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

 
