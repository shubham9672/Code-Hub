"""
    Program to swap two numbers without the use of additional temporary variable
"""
a = int(input("Enter the positive value of a : "))
b = int(input("Enter the positive value of b : "))
a = a + b
b = a - b
a = a - b
print(f"The value of a is : {a} \nThe value of b is : {b}")
