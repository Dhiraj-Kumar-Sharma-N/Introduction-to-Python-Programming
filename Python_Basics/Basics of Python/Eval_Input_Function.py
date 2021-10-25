# input ( ) : This function first takes the input from the user
# input() function only accepts String whatever is entered is considered as a string itself


# Program to check input type in Python

num = input("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))

"""

Enter number :10
10
Enter name : Dhiraj Kumar
Dhiraj Kumar
type of number <class 'str'>
type of name <class 'str'>

"""

#  Program to add two numbers taking input from the User in Python

a = int(input("Enter First Number = "))
b = int(input("Enter Second Number = "))

print(f'Sum of {a} and {b} is {a + b}')  # Sum of 10 and 20 is 1020 (Without int)

print(f'Sum of {a} and {b} is {a + b}') # Sum of 10 and 20 is 30

"""
Enter First Number = 2
Enter Second Number = 4
Sum of 2 and 4 is 6

"""

# eval is a built-in- function used in python, eval function parses the expression argument and evaluates it as a
# python expression. In simple words, the eval function evaluates the “String” like a python expression and returns
# the result as an integer.



#  Program to Multiply two numbers taking input from the User in Python

a = eval(input("Enter First Number = "))
b = eval(input("Enter Second Number = "))

print(f'Sum of {a} and {b} is {a * b}')  # Sum of 10 and 20 is 200 (Without int)


"""

Enter First Number = 1.56
Enter Second Number = 2.21
Sum of 1.56 and 2.21 is 3.4476

"""