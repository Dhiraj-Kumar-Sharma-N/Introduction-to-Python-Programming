import platform
import os

OS_Platform = platform.system()

print(f'It is a {OS_Platform} Platform')

if OS_Platform == "Windows":
    rt = os.system("cls")
elif OS_Platform == "Linux":
    rt = os.system("clear")
else:
    print("Invalid OS Platform")

print(rt)