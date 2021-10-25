"""

There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then


Operator	Description	Example
and Logical AND	If both the operands are true then condition becomes true.	(a and b) is true.
or Logical OR	If any of the two operands are non-zero then condition becomes true.	(a or b) is true.
not Logical NOT	Used to reverse the logical state of its operand.	Not(a and b) is false.


"""

a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("At least one number is not greater than 0")

"""
The numbers are greater than 0
At least one number is not greater than 0

"""

a = 10
b = 12
c = 0

if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("At least one number has boolean value as False")

#   At least one number has boolean value as False

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

"""

Either of the number is greater than 0
No number is greater than 0

"""

a = 10
b = 12
c = 0

if a or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")

# Atleast one number has boolean value as True

a = 10

if not a:
    print("Boolean value of a is True")

if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

# 10 is divisible by either 3 or 5
