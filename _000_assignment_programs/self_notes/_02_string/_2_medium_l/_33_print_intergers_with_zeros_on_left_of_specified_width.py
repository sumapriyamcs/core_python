'''
# P33. REQ :  print the following integers with zeros on the left of specified width
"""
1. CRUD       -->  update
2. STATE      -->  Int
3. BEHAVIOR   -->  int  |   +  =    |
"""

# 0. Mathematics
"""
1. take a number
2. convert that number into string
3.take one variable to store the result
4. use zfill with converted number and mention  zeros number with zfill how many zeros
you want to print before the number
#4.use number by using dot operation  with zfill function
4. pint the result

"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

a_number=11
number_str = str(a_number)
#Convert `a_number` to a string
zero_filled_number = number_str.zfill(3)
#Pad `number_str` with zeros to 5 digits
print(zero_filled_number)

print(format(5839, "*>8"))

# 2. Algorithm

print("--------2 Algorithm              ----------")
x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x))
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y))
print()

#3. by using functions:

def convert(x,y):
    print("\nOriginal Number: ", x)
    print("Formatted Number(left padding, width 2): " + "{:0>2d}".format(x))
    print("Original Number: ", y)
    print("Formatted Number(left padding, width 6): " + "{:0>6d}".format(y))
    print()
x = 3
y = 123
convert(x,y)


'''
