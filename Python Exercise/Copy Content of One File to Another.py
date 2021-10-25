Sourcefile = input(
    "Enter the Source file = ")  # 'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Other Files\\NewTextFile.txt'
Destinationfile = input(
    "Enter the Destination file = ")  # 'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Other Files\\CopiedTextFile.txt'
SF_fo = open(Sourcefile, 'r')
All_data = SF_fo.readlines()
SF_fo.close()

print(All_data)

DF_fo = open(Destinationfile, 'w')
for each_value in All_data:
    DF_fo.write(each_value)
DF_fo.close()

print("Content Copied Successfully")
