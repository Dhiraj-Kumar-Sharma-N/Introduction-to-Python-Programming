def addition(a, b):
    result = a + b
    return print(result)


def subtraction(a, b):
    result = a - b
    return print(result)


print("File1 __name__ = %s" % __name__)

if __name__ == "__main__":
    addition(2, 4)
    subtraction(5, 2)
    print("File1 is being run directly")
    print("This is Script1")

else:
    print("File1 is being imported")
