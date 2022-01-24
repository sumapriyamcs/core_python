'''
# P39. REQ :  reverse a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""
1. take a string
2. use slicing operation to reverse a string
3. to get the characters to reverse use -1 with slicing operation
4. finally,print the result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

s="suma priya"
print(s[::-1])

# 2. Algorithm
print("--------2 Algorithm              ----------")
str_1 = 'I am suma'
print("\nOriginal String : ", str_1)
print("Reverse String: ", str_1[::-1])
print()

#3. by using functions:

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)


# Python code to reverse a string
# using loop
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Geeksforgeeks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))


'''





