'''
# P57. REQ : remove spaces from a given string
"""
1. CRUD       -->  delete
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  ==    | for
"""

# 0. Mathematics
"""
str_1 = ' i am h un gry ! '
                ||
                --
expected o/p = iamhungry

"""
1. take a string from the user
2.to remove the spaces we will use replace builtin function

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

str_1 = ' i am h un gry ! '
print("String with space :", str_1)
print('String without space :', str_1.replace(' ', ''))

# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1="hello i a m o ka y"
str_2 = ''
print("String with space :", str_1)

for i in str_1:
    if i == ' ':
        str_2 += ""
    else:
        str_2 += i

print('String without space :', str_2)

#3.by using functions:

# Python3 code to remove whitespace
def remove(string):
	return string.replace(" ", "")

# Driver Program
string = ' g e e k '
print(remove(string))

'''


