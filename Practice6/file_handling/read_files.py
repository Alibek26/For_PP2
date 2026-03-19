# Open file in read mode ("r")
# If file does not exist → error will occur
with open("sample.txt", "r") as file:
    content = file.read()  # Read entire file content as string

# Print file content to console
print(content)