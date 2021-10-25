"""
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.

There are 7 arithmetic operators in Python :

Addition
Subtraction
Multiplication
Division
Modulus
Exponentiation
Floor division


Operator	             Description	                                                        Syntax
+	                Addition: adds two operands	                                                x + y
–	                Subtraction: subtracts two operands         	                            x – y
*	                Multiplication: multiplies two operands	                                    x * y
/	                Division (float): divides the first operand by the second	                x / y
//	                Division (floor): divides the first operand by the second	                x // y
%	                Modulus: returns the remainder when first operand is divided by the second	x % y
**	                Power : Returns first raised to power second	                            x ** y

"""

a = 10
b = 6
Result = a + b
print(f"Addition Result is : {Result}")  # Addition Result is : 16

a = 10
b = 6
Result = a - b
print(f"Subtraction Result  is : {Result}")  # Subtraction Result  is : 4

a = 10
b = 6
Result = a * b
print(f"Multiplication Result is : {Result}")  # Multiplication Result is : 60

a = 10
b = 6
Result = a / b
print(f"Division Result is : {Result}")  # Multiplication Result is : 1.66666666666667

a = 10
b = 6
Result = a // b  # Result is a Quotient
print(f"Floor Result is : {Result}")  # Floor Result is : 1

a = 14
b = 6
Result = a % b  # Result is a Reminder
print(f"Modules Result is : {Result}")  # Modules Result is : 2

a = 3
b = 4
Result = a ** b  # Result is a To the Power
print(f"Expo/Power Result is : {Result}")  # Expo/Power Result is : 81
