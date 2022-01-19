'''
# P01. REQ : program to check whether a string starts with special characters

"""
1. CRUD       - Retrieve
2. STATE      - String
3. BEHAVIOR   - str  | ==
"""

# 0. Mathematics

1. Initialize a string
2. retrieve the string with special character


# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

str1 = 'i am an idiot'
print("String :", str1)
print("String startswith 'i' :", str1.startswith('i'))
print("String startswith 'a' :", str1.startswith('a'))
print("String startswith 'I' :", str1.startswith('I'))

# 2. Algorithm

print("--------2 Algorithm              ----------")
str1="hello friends how are u"
print("String :", str1)
print("String startswith 'i' :", str1[0] == 'i')
print("String startswith 'I' :", str1[0] == 'I')

string = "w3resource.com"
print(string.startswith("aeiouAEIOU"))

str = "this is string example....wow!!!";
print (str.startswith( 'aeiou' ))
print (str.startswith( 'AEIOU' ))
print (str.startswith( 'this', 2, 4 ))

import string
sample_str = "sample string"
# Check if string starts with a special character
if sample_str[0] in string.punctuation:
    print("The String starts with a special character")
else:
    print("The String do not starts with a special character")

#3.using functions:

def check(str):
  import string
  # Check if string starts with a special character
  if str[0] in 'aeiouAEIOU':
      print("The String starts with a special character")
  else:
      print("The String do not starts with a special character")
str = "aasample string"
check(str)

'''