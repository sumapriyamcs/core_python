'''
# P45. REQ :  check if a string contains all letters of the alphabet
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |   >=  =    |
"""

# 0. Mathematics
"""
1. take a string
2.take a variable to check whether taken is in alpha are not
3. to check that use isalpha with string
4.prrint the result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
str1 = "hello world. welcome to python examples."
bool = str1.isalpha()
print('str1 contains only alphabets:', bool)



# 2. Algorithm

print("--------2 Algorithm              ----------")

import string
alphabet = set(string.ascii_lowercase)
str_1 = 'The quick brown fox jumps over the lazy dog'
print(set(str_1.lower()) >= alphabet)
str_2 = 'The quick brown fox jumps over the lazy cat'
print(set(str_2.lower()) >= alphabet)

#3. by using functions:

def find(str):

    import string
    alphabet = set(string.ascii_lowercase)
    str = 'We promptly judged antique ivory buckles for the next prize'
    print(set(str.lower()) >= alphabet)
find(str)

'''
