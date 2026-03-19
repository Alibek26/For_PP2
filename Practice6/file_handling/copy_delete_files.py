import shutil  # Used for copying files
import os      # Used for file existence and deletion

# Copy file (creates an exact duplicate)
shutil.copy("sample.txt", "sample_copy.txt")
print("File copied to sample_copy.txt")

# Create backup file
shutil.copy("sample.txt", "sample_backup.txt")
print("Backup created as sample_backup.txt")

# Define file to delete
file_to_delete = "sample_copy.txt"

# Check if file exists before deleting (safe deletion)
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)  # Delete file
    print(f"{file_to_delete} deleted successfully.")
else:
    print("File not found, nothing to delete.")