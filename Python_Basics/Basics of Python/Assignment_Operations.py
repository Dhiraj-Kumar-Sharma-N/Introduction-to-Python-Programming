"""

Assignment Operators are used to assigning values to variables.

Operator	Description     Syntax
=    Assign value of right side of expression to left side operand	x = y + z
+=   Add and Assign: Add right side operand with left side operand and then assign to left operand	a += b
-=   Subtract AND: Subtract right operand from left operand and then assign to left operand: True if both operands are equal	a -= b
*=   Multiply AND: Multiply right operand with left operand and then assign to left operand	a *= b
/=  Divide AND: Divide left operand with right operand and then assign to left operand	a /= b
%=  Modulus AND: Takes modulus using left and right operands and assign result to left operand	a %= b
//= Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a //= b
**= Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a **= b
&=  Performs Bitwise AND on operands and assign value to left operand	a &= b
|=  Performs Bitwise OR on operands and assign value to left operand	a |= b
^=  Performs Bitwise xOR on operands and assign value to left operand	a ^= b
>>= Performs Bitwise right shift on operands and assign value to left operand	a >>= b
<<= Performs Bitwise left shift on operands and assign value to left operand	a <<= b


"""
import a as a

a = 10
b = 6
a += b
print(f"Addition Result is : {a}")  # Addition Result is : 16

a = 10
b = 6
a -= b
print(f"Subtraction Result  is : {a}")  # Subtraction Result  is : 4

a = 10
b = 6
a *= b
print(f"Multiplication Result is : {a}")  # Multiplication Result is : 60

a = 10
b = 6
a /= b
print(f"Division Result is : {a}")  # Multiplication Result is : 1.66666666666667

a = 10
b = 6
a //= b  # Result is a Quotient
print(f"Floor Result is : {a}")  # Floor Result is : 1

a = 14
b = 6
a %= b  # Result is a Reminder
print(f"Modules Result is : {a}")  # Modules Result is : 2

a = 3
b = 4
a **= b  # Result is a To the Power
print(f"Expo/Power Result is : {a}")  # Expo/Power Result is : 81

a = 3
b = 5
a &= b
print(f"Bitwise AND Result is : {a}")  # Bitwise AND Result is : 1

a = 3
b = 5
a |= b
print(f"Bitwise OR Result is : {a}")  # Bitwise OR Result is : 7

a = 3
b = 5
a ^= b
print(f"Bitwise xOR Result is : {a}")  # Bitwise xOR Result is : 6

a = 3
b = 5
a >>= b
print(f"Bitwise right shift Result is : {a}")  # Bitwise right shift Result is : 0

a = 3
b = 5
a <<= b
print(f"Bitwise left shift Result is : {a}")  # Bitwise left shift Result is : 96
