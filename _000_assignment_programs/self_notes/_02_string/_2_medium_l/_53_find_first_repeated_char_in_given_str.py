'''

# P51. REQ :  find the first repeated character in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |   for, if
"""

# 0. Mathematics
"""
1. take a string
2.take on empty set to store result
3. use for loop to iterate characters present in the string
4.use if condition if the char present in empty set or not
5.if it is present print that char then break
5. it is not present store in empty set

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
letters = 'aacbdc'
found_dict = {}
for i in letters:
    if i in found_dict:
        print(i)
        break
    else:
        found_dict[i]= 1

# 2. Algorithm
print("--------2 Algorithm              ----------")
s="acdab"
for index, c in enumerate(s):
    if s[:index + 1].count(c) > 1:
       print(c)


str="ccodespeedy"
a=0
for i in range(0 , len(str) ):  #traversing through the entire string
    if a==1:
        break
    for j in range(i+1 , len(str)): #traversing characters after the current one
        if str[i]==str[j]:
            print(str[i])
            a=1              #this character is the first repeating character
            break
if a==0:
    print(-1)



# 3 Using Functions
print("--------3 Using Functions        ----------")


def first_repeated_char(str1):
    for index, c in enumerate(str1):
        if str1[:index + 1].count(c) > 1:
            return c
    return "None"


print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))

# Python program to find the first
# repeated character in a string
def firstRepeatedChar(str):

	h = {} # Create empty hash

	# Traverse each characters in string
	# in lower case order
	for ch in str:

		# If character is already present
		# in hash, return char
		if ch in h:
			return ch;

		# Add ch to hash
		else:
			h[ch] = 0

	return '\0'


# Driver code
print(firstRepeatedChar("geeksforgeeks"))

# Python implementation
from collections import Counter

# Function which repeats
# first repeating character
def printrepeated(string):

	# Calculating frequencies
	# using Counter function
	freq = Counter(string)

	# Traverse the string
	for i in string:
		if(freq[i] > 1):
			print(i)
			break


# Driver code
string = "geeksforgeeks"

# passing string to printrepeated function
printrepeated(string)

# this code is contributed by vikkycirus

'''
