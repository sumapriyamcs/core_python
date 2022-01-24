'''
# P41. REQ :  strip a set of characters from a string
"""
1. CRUD       -->  delete
2. STATE      -->  String
3. BEHAVIOR   -->  str  |   +=  =    | for if
"""

# 0. Mathematics
"""
1. take a string
2. use strip method with taken string to removes the spaces present in the string
3. to remove particular word use strip of that word with string.
4. to get the result use 2&3 steps in print statements
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# Python code to illustrate the working of strip()
string = ' Geeks for Geeks '

# Leading spaces are removed
print(string.strip())

# Geeks is removed
print(string.strip(' Geeks'))

# Not removed since the spaces do not match
print(string.strip('Geeks'))

# Python3 program to demonstrate the practical application
# strip()

string = " the King has the largest army in the entire world the"

# prints the string after removing the from beginning and end
print(string.strip(" the"))


# 2. Algorithm
print("--------2 Algorithm              ----------")

str_2 = "The quick brown fox jumps over the lazy dog."
print("String :", str_2)
st = 'aeiou'
s = ''
for i in str_2:
    if i not in st:
        s += i

print('Exp O/P : ', s)

#3. by using functions:

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

print("\nOriginal String: ")
print("The quick brown fox jumps over the lazy dog.")
print("After stripping a,e,i,o,u")
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
print()

'''



