# - enumerate() for indexed iteration
# - zip() for combining lists
# - type checking and type conversion

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# enumerate() returns pairs: (index, value)
print("Using enumerate():")
for index, name in enumerate(names):
    print(f"Index {index}: {name}")

# zip() combines multiple lists into pairs
print("\nUsing zip():")
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Type checking and conversion
value = "123"

# Check type
print("\nOriginal type:", type(value))

# Convert string to integer
num = int(value)
print("Converted to int:", num, type(num))

# Convert string to float
flt = float(value)
print("Converted to float:", flt, type(flt))

# Convert number back to string
text = str(num)
print("Converted back to string:", text, type(text))