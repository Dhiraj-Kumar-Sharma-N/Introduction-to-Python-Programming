import platform
import os
import string

OS_Platform = platform.system()
File_to_search = input("Enter File to Search =")
print(f'It is a {OS_Platform} Platform')
Base_path = "C:\\"

if OS_Platform == "Windows":
    print("This is a Windows System")
    possible_Drives = string.ascii_uppercase
    for drive in possible_Drives:
        if os.path.exists(drive+":\\"):
            Generated_Path = drive+":\\"
            print(Generated_Path)
            Base_path = Generated_Path
            for r, d, f in os.walk(Base_path):
                for file in f:
                    if file == File_to_search:
                        print(f'{File_to_search} FOUND AT : {os.path.join(r, File_to_search)}')
                        exit()
            break

elif OS_Platform == "Linux":
    print("This is a Linux System")
    Base_path = "/"
    for r, d, f in os.walk(Base_path):
        for file in f:
            if file == File_to_search:
                print(f'{File_to_search} FOUND AT : {os.path.join(r, File_to_search)}')
                exit()
else:
    print("Invalid OS Platform")
