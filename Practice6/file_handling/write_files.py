# Open file in write mode ("w")
# If file does not exist → it will be created
# If file exists → it will be overwritten
with open("sample.txt", "w") as file:
    file.write("Hello\n")  # Write first line
    file.write("Practice file handling\n")  # Write second line

# Open file in append mode ("a")
# This will NOT overwrite existing content
# It will add new lines to the end of the file
with open("sample.txt", "a") as file:
    file.write("Appended line\n")  # Add new line