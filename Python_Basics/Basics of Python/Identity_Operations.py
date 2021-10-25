"""

Identity operators compare the memory locations of two objects. There are two Identity operators explained below −

Operator	Description	Example

is	Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
x is y,here is results in 1 if id(x) equals id(y).


is not	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
x is not y, here is not results in 1 if id(x) is not equal to id(y).

"""

str1 = "Dhiraj"
int1 = 1
str2 = "Kumar"

print(str1 is str2)  # False
print(str1 is str1)  # True

print(type(str1) is type(str2))  # True
print(type(str1) is type(int1))  # False

print(type(str1) is not type(int1))  # True
