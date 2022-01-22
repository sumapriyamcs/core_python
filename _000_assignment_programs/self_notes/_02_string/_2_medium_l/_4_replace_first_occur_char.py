'''
# P04. REQ : Replace first occurrence character
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    |
"""

# 0. Mathematics
"""
str_1 = 'abc avd dvd'


o/p     'Abc avd dvd'
"""
1. take a string from the user
2.to replace the first character use replace function with string
3. use which character you want to replace with new character with index number
4. use above 2 and 3 statements in print statement to get the results

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
str_1 = 'abc avd dvd'
print("String : ", str_1)
print("Expected String :", str_1.replace('a', 'A', 1))

#2.algorithm:

str_1 = 'abc avd dvd'
print("String : ", str_1)
print("Expected String :", str_1.replace('a', 'A', 1))

#3.by using functions:

def replace(str_1):
    print("String : ", str_1)
    print("Expected String :", str_1.replace('a', 'A', 1))
str_1 = 'abc avd dvd'
replace(str_1)
'''
