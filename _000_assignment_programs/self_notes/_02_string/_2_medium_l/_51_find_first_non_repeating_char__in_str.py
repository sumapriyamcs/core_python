'''

# P51. REQ :  find the first non-repeating character in given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |  == +   =    |for if
"""

# 0. Mathematics
"""
1. take a string
2. use for loop to iterate characters present in the string
3.to find the first ocurence of character use find function with string
4.we will compare one character with another character that means i,i+1
5.that comparision characters equal to last index of character are not also we will check
6.if it is equal we wiil print the i value then break the statement


"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

s = 'geeksforgeeks'
for i in s:

        if (s.find(i,(s.find(i)+1))) == -1:

            print(i)

            break

# 2. Algorithm
print("--------2 Algorithm              ----------")

s = "tutorialspointfordeveloper"
while s != "":
   slen0 = len(s)
   ch = s[0]
   s = s.replace(ch, "")
   slen1 = len(s)
   if slen1 == slen0-1:
      print ("First non-repeating character is: ",ch)
      break;
   else:
         print ("No Unique Character Found!")

# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python implementation
from collections import Counter

# Function which repeats
# first Nonrepeating character
def printNonrepeated(string):

	# Calculating frequencies
	# using Counter function
	freq = Counter(string)
        #print(freq)

	# Traverse the string
	for i in string:
		if(freq[i] == 1):
			print(i)
			break


# Driver code
string = "geeksforgeeks"

# passing string to printNonrepeated function
printNonrepeated(string)

def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None


print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))


# python3 implementation

def FirstNonRepeat(s):

    for i in s:

        if (s.find(i,(s.find(i)+1))) == -1:

            print(i)

            break

    return

#__main__

s = 'geeksforgeeks'

FirstNonRepeat(s)




'''
