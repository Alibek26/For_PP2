import shutil
import os

# Ensure destination directory exists
os.makedirs("test_dir", exist_ok=True)

# Move file (removes from original location)
if os.path.exists("sample_backup.txt"):
    shutil.move("sample_backup.txt", "test_dir/sample_backup.txt")
    print("File moved to test_dir/")
else:
    print("sample_backup.txt not found")

# Copy file (keeps original file)
if os.path.exists("sample.txt"):
    shutil.copy("sample.txt", "test_dir/sample.txt")
    print("File copied to test_dir/")
else:
    print("sample.txt not found")