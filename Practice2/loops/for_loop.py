#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#Example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#Looping Through a String!!!
#Example
for x in "banana":
  print(x)  
  
#The range() Function!!!
#To loop through a set of code a specified number of times, we can use the range() function,
#The function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.range()
#Example 1
for x in range(6):
  print(x)
  
#Example 2
for x in range(2, 6):
  print(x)
  
#Example 3
for x in range(2, 30, 3):
  print(x)
  
#Else in For Loop!!!
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
#Example 1
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Example 2
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
#Nested Loops!!!
#A nested loop is a loop inside a loop.
#Example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
  