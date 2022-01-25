'''
# P50. REQ :  split a string on the last occurrence of the delimiter
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |  +   =    |
"""

# 0. Mathematics
"""
1. take a string
2. to split last occurence of delimiter use rsplit with taken string
3. split the string by using comma separator and use delimiter number
4. use 2 and 3 steps in print statement to get the result
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
str1 = 'I,AM,NOT,JOKER'
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))

#2. algorithm:

# Python3 code to demonstrate
# Split on last occurrence of delimiter
# using rsplit()

# initializing string
test_string = "gfg, is, good, better, and best"

# printing original string
print("The original string : " + str(test_string))

# using rsplit()
# Split on last occurrence of delimiter
res = test_string.rsplit(', ', 1)

# print result
print("The splitted list at the last comma : " + str(res))

#3. by using functions:

# Python3 code to demonstrate
# Split on last occurrence of delimiter
# using rsplit()

# initializing string
test_string = "gfg, is, good, better, and best"

# printing original string
print("The original string : " + str(test_string))

# using rsplit()
# Split on last occurrence of delimiter
res = test_string.rsplit(', ', 1)

# print result
print("The splitted list at the last comma : " + str(res))

s = 'canada-japan-australia-uae-india'
l = s.rsplit('-', 1)[1]
print(l)

#3. by using functions:

def sep(str):

    result = str.rsplit(",", 1)

    print(result)

str = "a,b,c,defgh"
sep(str)

'''

