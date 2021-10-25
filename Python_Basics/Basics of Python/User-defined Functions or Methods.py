"""

Function is block of code for a specific operation
function code is re-usable,Modularity
it will execute only when it is called

Syntax:
        def Function/Method_Name (Arguments):

Function name should be a-z,A-Z,0-9,_
function name should be lower case and should not start with number but can start with _
function name should not include any spaces
function must be defined before calling it


Any variable declared inside a function is a local variable and cannot be accessed outside the function
Any variable declared inside a function is a Global variable and can be accessed outside and inside the function

"""

import os
import platform
import time


def my_method(cmd1, cmd2):
    print("Cleaning the screen")
    time.sleep(2)
    os.system(cmd1)
    print("Printing the Directory list")
    time.sleep(2)
    os.system(cmd2)
    return platform.system()


def main():
    if platform.system() == "Windows":
        platform_name = my_method("cls", "dir")
        print(f'Platform is {platform_name}')
    else:
        platform_name = my_method("clear", "ls -ltr")
        print(f'Platform is {platform_name}')


main()


# =========================== default values for Arguments =====================================

def display_input(value=0):  # Assigned  0 value as default
    print("Entered value is = ", value)


display_input(6)  # Entered value is =  6
display_input(3)  # Entered value is =  3
display_input()  # Entered value is =  0


# Parameter/Argument which has a default value should always be at the end of the argument list

def display_sum(value1, value2=0):  # Assigned  0 value as default
    result = value1 + value2
    print("sum of values is = ", result)


display_sum(10, 20)  # sum of values is =  30
display_sum(10)  # sum of values is =  10


# display_sum()  # FAILED

# =========================== functions with keyword based arguments =====================================

def display_input(value1, value2):
    print("Entered first value is = ", value1)


display_input(6, "Dhiraj")  # Entered first value is =  6
display_input("Dhiraj", 6)  # Entered first value is =  Dhiraj

# if we want a value to be assigned to particular variable in method we need to use Keyword based arguments

display_input(value1=6, value2="Dhiraj")  # Entered first value is =  6
display_input(value2="Dhiraj", value1=6)  # Entered first value is =  6


# =========================== functions with variable length of arguments =====================================

def display_type(*value):  # * indicated variable length of arguments stored in tuple
    for each in value:
        print("type of value is = ", type(each))
        print(each)


display_type()
display_type(4)
display_type("dhiraj")
display_type(4, "dhiraj", 5.77)

"""
type of value is =  <class 'int'>
4
type of value is =  <class 'str'>
dhiraj
type of value is =  <class 'int'>
4
type of value is =  <class 'str'>
dhiraj
type of value is =  <class 'float'>
5.77

"""


# =========================== functions with variable length of keyword arguments =====================================

def display_value(**value):  # * indicated variable length of keyword arguments stored in Dictionary
    print(value)


display_value(a=5)
display_value(b=5, a=6)
display_value(a="dhiraj", b=5, c=4.2)

"""

{'a': 5}
{'b': 5, 'a': 6}
{'a': 'dhiraj', 'b': 5, 'c': 4.2}

"""


def display_value1(x, **value):  # * indicated variable length of keyword arguments stored in Dictionary
    print(x)
    value[x] = x
    print(value)


display_value1(10, a=5)
display_value1(x=5, b=5, a=6)
display_value1(x="sharma", a="dhiraj", b=5, c=4.2)

"""

10
{'a': 5, 10: 10}
5
{'b': 5, 'a': 6, 5: 5}
sharma
{'a': 'dhiraj', 'b': 5, 'c': 4.2, 'sharma': 'sharma'}

"""