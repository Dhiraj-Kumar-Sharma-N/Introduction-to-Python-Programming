import csv

# =============================== READ : USING CSV ===================================

File_Path = 'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Other Files\\SampleCsvFile.csv'
FileObject = open(File_Path, 'r')
CSVObj = csv.reader(FileObject)
for each_r in CSVObj:
    print(each_r)
FileObject.close()

# =============================== WRITE : USING CSV ===================================

File_Path = 'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Other Files\\CreatedCsvFile.csv'
FileObject = open(File_Path, 'w', newline="")
CSVObj = csv.writer(FileObject, delimiter=",")
CSVObj.writerow(['Sl.no', 'Book Name', 'Author'])  # Single Line write
CSVObj.writerow(['1', 'C# Tutorials', 'Arnold'])
CSVObj.writerow(['2', 'Ruby on Rails', 'Jhon Snow'])
FileObject.close()

# =============================== READ ONLY HEADER : USING CSV ===================================

File_Path = 'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Other Files\\SampleCsvFile.csv'
FileObject = open(File_Path, 'r')
CSVObj = csv.reader(FileObject)
All_rows = list(CSVObj)
print("The header of the file is = ", All_rows[0])
print("Total Number of Rows in the file is = ", len(All_rows[0]) - 1)
FileObject.close()

File_Path = 'C:\\Users\\dsharman\\Python_Workspace\\Python_Basics\\Other Files\\CreatedCsvFile.csv'
FileObject = open(File_Path, 'r')
CSVObj = csv.reader(FileObject)
Header = next(CSVObj)
print("The header of the file is = ", Header)
print("Total Number of Rows in the file is = ", len(list(CSVObj)))
FileObject.close()

# C:\Users\dsharman\Python_Workspace\venv\Scripts\python.exe "C:/Users/dsharman/Python_Workspace/Python_Basics/Basics of Python/Working with Excel Files.py"
# ['EMPLOYEE ID', 'NAME', 'SALARY', 'AGE']
# ['101', 'DHIRAJ', '100$', '27']
# ['102', 'KUMAR', '220$', '30']
# ['103', 'SHARMA', '500$', '99']
# The header of the file is =  ['EMPLOYEE ID', 'NAME', 'SALARY', 'AGE']
# Total Number of Rows in the file is =  3
# The header of the file is =  ['Sl.no', 'Book Name', 'Author']
# Total Number of Rows in the file is =  2
