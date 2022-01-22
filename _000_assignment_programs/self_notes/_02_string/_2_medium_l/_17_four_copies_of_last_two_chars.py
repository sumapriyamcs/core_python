'''
# P017. REQ : 4 Copies of last 2 chars
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |    =   * - |
"""

# 0. Mathematics
"""
str_1 = 'i am ila'

exp. o/p = lalalala
"""
1. take a string from the user
2. use index number of last two characters of string, to use that we will use slicing operation
3.to print that characters four times use star operation with how many times
you want to print that characters
4. print that result finally

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
mystr = "abcdefghijkl"
print(mystr[-2:]*4)

# 2. Algorithm
print("--------2 Algorithm              ----------")

str_1 = 'i am ila'
print("String :", str_1)
print("Exp. String :", str_1[-2:]*4)

#by using functions:

def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))

'''

