'''
# P01. REQ : print the index of the character in a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  +=  =    | for
"""

# 0. Mathematics
"""
1. Initialize the string
2. Retrieve the index of chars

str_1 = "abcdxyz"
index=>  0123456
"""

# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2.use for loop to iterate characetrs present in the string
3.to print the index of every character use index of every character with in print statement

"""
print("--------1 Builtin Functions      ----------")
str_1 = "abcdxyz"
print("String :", str_1)
for i in str_1:
    print("%s" % i, "index is ", str_1.index(i))

# 2. Algorithm

print("--------2 Algorithm              ----------")

j = 0
str_1 = "abcdxyz"
print("String :", str_1)

for i in str_1:
    print(i, "index is ", j)
    j += 1

#3.using functions:

def index(str_1):

    j = 0
    print("String :", str_1)

    for i in str_1:
        print(i, "index is ", j)
        j += 1
str_1 = "abcdxyz"
index(str_1)
'''

