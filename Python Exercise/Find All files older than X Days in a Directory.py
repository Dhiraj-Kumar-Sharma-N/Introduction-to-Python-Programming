import os
import sys
import datetime

Entered_path = input("Enter the path = ")
if os.path.exists(Entered_path):
    print("Valid Path Entered")
    Req_Date = input('Enter Number of X Days = ')
    List_of_files_dir = os.listdir(Entered_path)
    print(List_of_files_dir)
    for each_file_dir in List_of_files_dir:
        generated_path = os.path.join(Entered_path, each_file_dir)
        if os.path.isfile(generated_path):
            Create_time = os.path.getctime(generated_path)
            Format_create_time = datetime.datetime.fromtimestamp(Create_time)
            Current_Time = datetime.datetime.now()
            # print(Current_Time)
            # print(generated_path, Format_create_time)
            Diff_dates = (Current_Time - Format_create_time).days

            if Diff_dates <= int(Req_Date):
                print(f'{generated_path} is {Diff_dates} days old from Current Date')

else:
    print("Invalid Path Entered")
    sys.exit()

# Enter the path = C:\Users\dsharman\OneDrive - HARMAN\Desktop\Allfiles
# Valid Path Entered
# Enter Number of X Days = 50
# ['A.csv', 'Autobahn Automation KT - Venkata 2021-07-22-15-01-49.mp4', 'B.csv', 'cfgB.json', 'dif.csv', 'DiffFiles', 'origA.csv', 'origB.csv', 'OUTPUT', 'output.csv', 'ParamConfig.properties', 'qcReducer.py', 'RentAgreement.docx', 'Sample.py', 'test.py', 'TextA.txt', 'TextB.txt', 'xml-comparison.log']
# C:\Users\dsharman\OneDrive - HARMAN\Desktop\Allfiles\RentAgreement.docx is 31 days old from Current Date
# C:\Users\dsharman\OneDrive - HARMAN\Desktop\Allfiles\Sample.py is 48 days old from Current Date
# C:\Users\dsharman\OneDrive - HARMAN\Desktop\Allfiles\xml-comparison.log is 48 days old from Current Date
