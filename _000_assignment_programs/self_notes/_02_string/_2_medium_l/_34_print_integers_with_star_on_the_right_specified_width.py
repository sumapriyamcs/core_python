'''
# P34. REQ :  print the following integers with '*' on the right of specified width
"""
1. CRUD       -->  update
2. STATE      -->  Int
3. BEHAVIOR   -->  int  |     =    |
"""
print("Formatted Number(right padding, width 0): "+"{:*< 6d}".format(x))
# 0. Mathematics
"""
1.take a number
2. use print stement to get the result
3. within in print statement use right padding statement and use width number how much you want
4. after , gave the width use plus symbol to separate the statement
5. then, within flower braces use slicing operation, in slicing in end point
use start with lesss than symbol
and give , with how many digits you want to compare a width
6. after that use .format with taken number


"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

x=22
print(format(5839, "*<8"))
print("Formatted Number(right padding, width 0): "+"{:*< 6d}".format(x))


# 2. Algorithm
print("--------2 Algorithm              ----------")
x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x))
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y))
print()

#by using functions:

def right(x):
    print(format(5839, "*<8"))
    print("Formatted Number(right padding, width 0): " + "{:*< 6d}".format(x))
x = 22
right(x)

'''

