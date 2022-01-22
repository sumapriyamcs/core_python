'''

# P20. REQ :  reverses a string if it's length is a multiple of 4
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  int  |     =    |     if
"""
# 0. Mathematics
"""
str_1 = 'i am the python engineer    '

o/p  =  '     reenigne nohtyp eht ma i'
"""
1. take a string from  user
2. print length of string
3.use if condition if length of string ismodule of four or not
4. if the length of string is module of four we will reverse that string by using slicing operation.
5. to reverse the string we start from negative index onwards
6.use 4&5 points within pint statement to get result

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

str_1 = 'i am the python engineer    '
print("String :", len(str_1))
if len(str_1) % 4 == 0:
    print("String reverse order :", str_1[::-1])

# 2. Algorithm
print("--------2 Algorithm              ----------")

name=input("enter a name:")

if(len(name)%4==0):
    print(name[::-1])
else:
    print("cant")

#by using functions:

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))

'''
