'''

# P43. REQ :  square and cube symbol in the area of a rectangle and volume of a cylinder
"""
1. CRUD       -->  update
2. STATE      -->  Float
3. BEHAVIOR   -->  int  |     =    |
"""

# 0. Mathematics
"""
1. take a area and volume
2.take a decimals
3.use slicing operation with in set data structure, starting is 0 and end is 1
use 1 within flower braces with dot operation and use format function f
4. use sstep3 with cm and module of decimal numbers in binary way(like u00b2)
5. after that use .with format function and with area and decimals
6. to get the results use 3&4&5 steps with in print statement
7.for voulme also we should do same thing

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
area = 1256.66
volume = 1254.725
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))

# 2. Algorithm
print("--------2 Algorithm              ----------")
area = 1256.66
volume = 1254.725
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))

#3. by using functions:

def symbol(area,volume):
    decimals = 2
    print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
    decimals = 3
    print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))
area = 1256.66
volume = 1254.725
symbol(area,volume)

'''


