# P01. REQ : to display a number with a comma separator
"""
1. CRUD       -->  Retrieval
2. STATE      -->  Integer
3. BEHAVIOR   -->  int  |  =   ,    |
"""

# 0. Mathematics

"""
1. Initialize the number
2. separate the number with coma and retrieve 
a = 100000000000
    100,000,000,000
"""
# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
numbers = "{:,}".format(5000000)
print(numbers)

# 2. Algorithm

print("--------2 Algorithm              ----------")

x = 3000000
y = 300000000000
print("Original Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x))
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y))

#3.by using functions:

def comma(x,y):
    print("Original Number: ", x)
    print("Formatted Number with comma separator: "+"{:,}".format(x))
    print("Original Number: ", y)
    print("Formatted Number with comma separator: "+"{:,}".format(y))
x = 3000000
y = 300000000000
comma(x,y)



