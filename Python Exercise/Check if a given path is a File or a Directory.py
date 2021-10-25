import os

Entered_path = input("Enter the path = ")
if os.path.exists(Entered_path):
    print("Valid Path Entered")
    if os.path.isdir(Entered_path):
        print(f"{Entered_path} is a Directory")
    else :
        print(f"{Entered_path} is a File")
else:
    print("Invalid Path Entered")