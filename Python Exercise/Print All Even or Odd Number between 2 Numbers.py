Start_point = input('Enter the Starting Number ')
End_point = input('Enter the Ending Number ')
Even_list = []
Odd_List = []

for each_num in range(int(Start_point), int(End_point) + 1):
    if each_num % 2 == 0:
        Even_list.append(each_num)

    else:
        Odd_List.append(each_num)

print(f'Even Numbers are : {Even_list}')
print(f'Odd Numbers are : {Odd_List}')

# Enter the Starting Number 0
# Enter the Ending Number 10
# Even Numbers are : [0, 2, 4, 6, 8, 10]
# Odd Numbers are : [1, 3, 5, 7, 9]
