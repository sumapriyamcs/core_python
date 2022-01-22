'''
# P18. REQ : Length of first 3 chars
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |    =    |
"""

# 0. Mathematics
"""
str_1 = 'back to pavilion '
o/p   = 3
"""
1.take a string
2.use len function to string to get length
3. use slicing operation to string to get the first three characters of string
4. use 2&3 steps with in print statement to get result

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

string = 'This is a string'
print(len(string[:3]))

# 2. Algorithm
print("--------2 Algorithm              ----------")

str_1 = 'back to pavilion '
print("String :", str_1)
print("Length of 1st 3 chars :", len(str_1[:3]))

str="hello world"
# Get First 3 character of a string in python
first_chars = sample_str[0:3]
print('First 3 characters: ', first_chars)

#by using functions:

def get(str):

    print(len(str[:3]))

str = 'This is a string'
get(str)
'''
