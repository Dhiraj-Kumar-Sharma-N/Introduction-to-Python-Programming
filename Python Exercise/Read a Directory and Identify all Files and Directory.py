import os
import sys

Entered_path = input("Enter the path = ")
if os.path.exists(Entered_path):
    print("Valid Path Entered")
    List_of_files_dir = os.listdir(Entered_path)
    print(List_of_files_dir)
    for each_file_dir in List_of_files_dir:
        generated_path = os.path.join(Entered_path,each_file_dir)
        if os.path.isdir(generated_path):
            print(f"{generated_path} is a Directory")
        else:
            print(f"{generated_path} is a File")
else:
    print("Invalid Path Entered")
    sys.exit()