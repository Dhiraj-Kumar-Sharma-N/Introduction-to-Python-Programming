# ============================= ModuleNotFoundError ================================
"""
import xlrd

Traceback (most recent call last):
  File "C:/Users/dsharman/Python_Workspace/Python_Basics/Basics of Python/Exception Handling.py", line 1, in <module>
    import xlrd
ModuleNotFoundError: No module named 'xlrd'

"""

try:
    import xlrd
except Exception as e:
    print(e)  # No module named 'xlrd'
print("ModuleNotFoundError handled Successfully")

# ============================= ZeroDivisionError ================================

try:
    print(4 / 0)
except Exception as e:
    print(e)  # division by zero
print("ZeroDivisionError handled Successfully")

# ============================= FileNotFoundError ================================

try:
    fo = open('No_file.txt')
    data = fo.read()
    fo.close()
except Exception as e:
    print(e)  # [Errno 2] No such file or directory: 'No_file.txt'
print("FileNotFoundError handled Successfully")

# ============================= IndexError ================================

My_List = [1, 2, 3, 4]

try:
    print(My_List[4])
except Exception as e:
    print(e)  # list index out of range
print("IndexError handled Successfully")

# ============================= NameError ================================

try:
    print(Var)
except Exception as e:
    print(e)  # name 'Var' is not defined
print("NameError handled Successfully")

# ============================= TypeError ================================

try:
    print(1 + "String")
except Exception as e:
    print(e)  # unsupported operand type(s) for +: 'int' and 'str'
print("TypeError handled Successfully")

# ============================= Exception handling on known Errors ================================

try:
    import xlrd
except ModuleNotFoundError:
    print("Module Needs to be imported")
    print("TypeError handled Successfully")

My_List = [1, 2, 3, 4]

try:
    fo = open('No_file.txt')
    data = fo.read()
    fo.close()
    print(My_List[4])
    print(Var)
    print(4 / 0)
    print(1 + "String")
except TypeError:
    print("String cannot be concatenated to int")
    print("TypeError handled Successfully")
except ZeroDivisionError:
    print("Number cannot be divided by 0")
    print("ZeroDivisionError handled Successfully")
except NameError:
    print("Variable not declared")
    print("NameError handled Successfully")
except IndexError:
    print("Index out of range")
    print("IndexError handled Successfully")
except FileNotFoundError:
    print("File does not Exists")
    print("FileNotFoundError handled Successfully")
except Exception as e:
    print(e)
finally:
    print("Execute after try and except block irrespective of Error")

"""

No module named 'xlrd'
ModuleNotFoundError handled Successfully
division by zero
ZeroDivisionError handled Successfully
[Errno 2] No such file or directory: 'No_file.txt'
FileNotFoundError handled Successfully
list index out of range
IndexError handled Successfully
name 'Var' is not defined
NameError handled Successfully
unsupported operand type(s) for +: 'int' and 'str'
TypeError handled Successfully
Module Needs to be imported
TypeError handled Successfully
File does not Exists
FileNotFoundError handled Successfully
Execute after try and except block irrespective of Error

"""

# ============================= Exception handling with Try except finally else Block ================================

try:
    Var = 1
    print(Var)
except NameError:
    print("Variable not declared")
    print("NameError handled Successfully")
except Exception as e:
    print(e)
else:
    print("If Try block does not have any exception then Else block is Executed")
finally:
    print("Execute after try and except block irrespective of Error")

# =============================Generate Custom Exception  ================================
"""

raise : Used to generate known/existing Custom exceptions 
assert : used to create an Assertion error exception

raise NameError("Custom Exception raised using RAISE Keyword")

Traceback (most recent call last):
  File "C:/Users/dsharman/Python_Workspace/Python_Basics/Basics of Python/Exception Handling.py", line 139, in <module>
    raise NameError("Custom Exception raised using RAISE Keyword")
NameError: Custom Exception raised using RAISE Keyword

"""

Age = 27

if Age < 25:
    print("VALID AGE")
else:
    raise ValueError(
        "Enter valid age : Generated Custom Exception")

# ValueError: Enter valid age : Generated Custom Exception

Age1 = 20

try:
    assert Age1 > 25
    print("VALID AGE")
except AssertionError:
    print("Error Created using Assertion Error")
except Exception as e:
    print(e)

#   Error Created using Assertion Error
