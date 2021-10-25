"""

Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
There are two membership operators as explained below −


Operator	Description	Example
in	Evaluates to true if it finds a variable in the specified sequence and false otherwise.
x in y, here in results in a 1 if x is a member of sequence y.


not in	Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
x not in y, here not in results in a 1 if x is not a member of sequence y.


"""

list1 = [2, 7, 9, 0]
Search_Var = 2
Search_Var1 = 6

print(Search_Var in list1) # True
print(Search_Var1 in list1) # False

print(Search_Var1 not in list1) # True
print(Search_Var not in list1) # False
