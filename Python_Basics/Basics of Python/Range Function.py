"""

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

Syntax
range(start, stop, step)
Parameter Values
Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

"""

print(range(0, 5))  # range(0, 5)

print(type(range(0, 5)))  # <class 'range'>

print(list(range(0, 5)))  # [0, 1, 2, 3, 4]

print(list(range(3)))  # [0, 1, 2]

print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

print(list(range(0, 20, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(list(range(0, 27, 7)))  # [0, 7, 14, 21]

print(list(range(10, 5)))  # []

print(list(range(10, 5, -1)))  # [10, 9, 8, 7, 6]

print(list(range(-10, -5, 1)))  # [-10, -9, -8, -7, -6]

print(list(range(10, -5, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

print(list(range(0, 101, 2)))  # Even Numbers from 0 to 100

print(list(range(1, 101, 2)))  # Odd Numbers from 0 to 100

List_obj = [6, 'Dhiraj', 9, 'Kumar']

for each_obj in range(len(List_obj)):
    print(f'index : {each_obj} ==> Value : {List_obj[each_obj]}')

# index : 0 ==> Value : 6
# index : 1 ==> Value : Dhiraj
# index : 2 ==> Value : 9
# index : 3 ==> Value : Kumar
