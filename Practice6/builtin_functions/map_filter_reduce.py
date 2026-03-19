from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

# map() applies a function to every element
# Here we square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# filter() keeps only elements that satisfy a condition
# Here we keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce() aggregates values into a single result
# Here we calculate the sum of all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)