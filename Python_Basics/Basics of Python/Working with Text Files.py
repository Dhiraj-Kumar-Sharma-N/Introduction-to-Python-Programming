"""
OPEN File = w > write mode
            a > append mode
            r > read mode

on W mode if the file exist content is overwritten
          if the file does not exists a new file is created

on A mode if the file exist content is appended
          if the file does not exists a new file is created

By default if no mode is provided as argument it is in Read Mode

"""

my_details = ['Dhirajkumar643@yahoo.in\n', '9535802575\n', 'Bangalore\n']
fo = open('../Other Files/NewTextFile.txt', 'w')
print(fo.writable())  # True
print(fo.readable())  # False
fo.write("Dhiraj Kumar Sharma N\n")
fo.write("Automation Specialist\n")
fo.writelines(my_details)
fo.close()

fo1 = open('../Other Files/NewTextFile.txt', 'a')
fo1.write("India")
fo1.close()

# Read all data once

fo2 = open('../Other Files/NewTextFile.txt', 'r')
All_Data = fo2.read()
fo2.close()
print(All_Data)

# Dhiraj Kumar Sharma N
# Automation Specialist
# Dhirajkumar643@yahoo.in
# 9535802575
# Bangalore
# India

# Read data one line by line

fo2 = open('../Other Files/NewTextFile.txt', 'r')
print(fo2.readline())  # Dhiraj Kumar Sharma N
print(fo2.readline())  # Automation Specialist
fo2.close()


fo2 = open('../Other Files/NewTextFile.txt', 'r')
print(fo2.readlines())  # ['Dhiraj Kumar Sharma N\n', 'Automation Specialist\n', 'Dhirajkumar643@yahoo.in\n', '9535802575\n', 'Bangalore\n', 'India']
fo2.close()

