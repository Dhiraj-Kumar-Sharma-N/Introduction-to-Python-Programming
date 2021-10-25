import os

Entered_Directory = input('Enter the Directory = ')

if os.path.exists(Entered_Directory):
    print("The Entered Path is a Valid Path")
    entered_extension = input('Enter the Extension of File to Search = ')
    List_of_Files = os.listdir(Entered_Directory)
    Req_List = []
    if len(List_of_Files) != 0:
        for each_file in List_of_Files:
            if each_file.endswith(entered_extension):
                Req_List.append(each_file)
    else:
        print("The entered Directory does not have any Files")
else:
    print("The Entered Path is a In-Valid Path")

print(f'Entered path = {Entered_Directory} has {Req_List} files with {entered_extension} extension')

# The Entered Path is a Valid Path
# Enter the Extension of File to Search = .json
# Entered path = C:\Users\dsharman\OneDrive - HARMAN\Desktop\Allfiles has ['cfgB.json'] files with .json extension
