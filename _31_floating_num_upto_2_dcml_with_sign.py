# P01. REQ : to print the following floating numbers up to 2 decimal places with sign

"""
1. CRUD       - Retrieve
2. STATE      - Float
3. BEHAVIOR   - =
"""

# 0. Mathematics
'''
1. Define the float number 
2. Retrieve up to 2 digit decimal point with sign
'''

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
x = 3.1415926
y = -12.9999
print("Original 1st Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x))
print("Original 2nd Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y))

# 2. Algorithm

print("--------2 Algorithm              ----------")
x = 3.1415926
y = -12.9999
print("Original 1st Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x))
print("Original 2nd Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y))

#3.by using functions:

def sign(x, y):
    print("\nOriginal Number: ", x)
    print("Formatted Number with sign: " + "{:+.2f}".format(x));
    print("Original Number: ", y)
    print("Formatted Number with sign: " + "{:+.2f}".format(y));
    print()

x = 3.1415926
y = -12.9999
sign(x, y)