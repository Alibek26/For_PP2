import os

# Create nested directories
# exist_ok=True prevents error if folders already exist
os.makedirs("test_dir/subdir1/subdir2", exist_ok=True)
print("Directories created successfully.")

# List all files and folders in current directory
print("\nDirectory contents:")
for item in os.listdir("."):
    print(item)  # Print each file/folder name

# Find all .txt files in current directory
print("\nSearching for .txt files:")
for file in os.listdir("."):
    if file.endswith(".txt"):  # Check file extension
        print(file)