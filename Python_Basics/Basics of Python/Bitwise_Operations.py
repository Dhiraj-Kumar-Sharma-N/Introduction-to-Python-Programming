"""

Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""

print(10 & 5)  # 0
print(10 & 10)  # 10

print(10 | 5)  # 15
print(10 | 10)  # 10

print(10 ^ 5)  # 15
print(10 ^ 10)  # 0

print(10 << 5)  # 320
print(10 << 10)  # 10240


print(10 >> 5)  # 0
print(10 >> 10)  # 0