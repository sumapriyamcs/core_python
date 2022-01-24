'''
# P32. REQ :  print the following floating numbers with no decimal places
"""
1. CRUD       -->  Retrieval
2. STATE      -->  Float
3. BEHAVIOR   -->  int  |     =    |
"""

# 0. Mathematics
"""
1. take a float number
2. to pint that number without decimal point use round of taken number within
print statement.

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
n=12.3030
print(round(n))

# 2. Algorithm

print("--------2 Algorithm              ----------")
x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x))
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y))
print()


Number1 = 44.560
Number2 = 856.9785623
Number3 = 9999.99

# Type conversion float to int
New_Number1 = int(Number1)
New_Number2 = int(Number2)
New_Number3 = int(Number3)

print("Number1 = ", New_Number1)
print("Number2 = ", New_Number2)
print("Number3 = ", New_Number3)

# type() function returns the data type
print(type(Number1))
print(type(New_Number1))


# import math function to use trunc( ) function
import math

num1 = math.trunc(450.63)
print(num1)
print(math.trunc(999998.99999))
print(math.trunc(-89.99))
print(math.trunc(0.99))

#3. by using functions:

def remove(num_values):

    sp_lst = []
    for ele in num_values:
        sp_lst.append(str(ele).split('.')[0])
    sp_lst = [int(i) for i in sp_lst]
    print("The resultant list is: ", sp_lst)
num_values=[523.771,21.67,182.33,211.54,19.1]
remove(num_values)

'''


