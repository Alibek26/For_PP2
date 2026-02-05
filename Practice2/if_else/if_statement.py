"""
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
"""

#An "if statement" is written by using the if keyword!!!
#Example 1
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#Example 2
number = 15
if number > 0:
  print("The number is positive")
  
#Multiple Statements in If Block!!!
#Example
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Using Variables in Conditions!!!
#Example: Using a boolean variable
is_logged_in = True
if is_logged_in:
  print("Welcome back!")