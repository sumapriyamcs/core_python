'''

# P61. REQ :   remove duplicate characters of a given string
"""
1. CRUD       -->  delete
2. STATE      -->  String
3. BEHAVIOR   -->   str    |  +   =    |for if/else
"""

# 0. Mathematics
"""
1. take a string
2.to remove duplicate characters present in the string use set data structure
3. after removing duplicate characters join unique characters left in the string
4. print the result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

s = "Protijayi"

aa = [ ch  for i, ch in enumerate(s) if ch not in s[:i]]
print(''.join(aa))

s = 'ppppmm'
s = ''.join(set(s))
print(s)

# 2. Algorithm
print("--------2 Algorithm              ----------")


string = "Protiijaayiiii"
s = set()
list = []
for ch in string:
    if ch not in s:
        s.add(ch)
        list.append(ch)

print(''.join(list))


# 3 Using Functions
print("--------3 Using Functions        ----------")

from collections import OrderedDict
str_1 = "sumapriya"


def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))



print(remove_duplicate(str_1))



def removeDuplicate(str):
	s=set(str)
	s="".join(s)
	print("Without Order:",s)
	t=""
	for i in str:
		if(i in t):
			pass
		else:
			t=t+i
		print("With Order:",t)

str="geeksforgeeks"
removeDuplicate(str)


# Python program to remove duplicate character
# from character array and print in sorted
# order
def removeDuplicate(str, n):
	s = set()

	# Create a set using String characters
	for i in str:
		s.add(i)

	# Print content of the set
	st = ""
	for i in s:
		st = st+i
	return st


# Driver code
str = "geeksforgeeks"
n = len(str)
print(removeDuplicate(list(str), n))

# This code is contributed by rajsanghavi9.


'''



