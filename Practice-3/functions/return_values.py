#Return Values!!!
#Functions can send data back to the code that called them using the return statement.
#Example 1
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#Example 2
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#Example 3
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#Example 4
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#Example 5
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Example 6
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

