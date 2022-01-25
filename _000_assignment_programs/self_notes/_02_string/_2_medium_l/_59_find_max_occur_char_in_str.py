'''
# P59. REQ :   find the maximum occurring character in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
"""

# 0. Mathematics
"""
Step 1- Define a string with characters

Step 2- Declare an empty dictionary

Step 3- Run a loop to iterate through the string

Step 4- Add the character in the dictionary and keep a count of the frequency

Step 5- To get the maximum count use max() and store the value returned by it in a variable

Step 6- Print the variable which has the lowest count as the result

                    (and)
Step 1- Import Counter

Step 2- Declare a string with characters

Step 3- Print string

Step 4- Call the Counter() and pass the string

Step 5- To get the maximum count use max() and store the value returned by it in a variable

Step 6- Print the variable as the result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
string= "mississippis"
print(string)

char_freq={}

for i in string:
    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i] = 1
result= max(char_freq, key = char_freq.get)

print("Most frequent character: ",result)

from collections import Counter

string= "pppppppghhhijeuupffe"
print(string)

result= Counter(string)
result= max(result, key=result.get)

print("Most frequent character: ",result)

# 2. Algorithm
print("--------2 Algorithm              ----------")
# Python 3 code to demonstrate
# Maximum frequency character in String
# collections.Counter() + max()
from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print ("The original string is : " + test_str)

# using collections.Counter() + max() to get
# Maximum frequency character in String
res = Counter(test_str)
res = max(res, key = res.get)

# printing result
print ("The maximum of all characters in GeeksforGeeks is : " + str(res))



# Python program to find the
# maximum frequency character of the string

import collections
# Getting string input from the user
myStr =  input('Enter the string : ')

# Finding the maximum frequency character of the string
freq = freq = collections.Counter(myStr)
maxFreqChar = max(freq, key = freq.get)

# Printing values
print("Entered String is ", myStr)
print(maxFreqChar , "is the maximum frequency character with frequency of " , freq[maxFreqChar])


# Python program to find the
# maximum frequency character in the string

# Getting string input from the user
myStr =  input('Enter the string : ')

# Finding the maximum frequency character of the string
freq = {}
for i in myStr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maxFreqChar = max(freq, key = freq.get)

# Printing values
print("Entered String is ", myStr)
print(maxFreqChar , "is the maximum frequency character with frequency of " , freq[maxFreqChar])



# 3 Using Functions
print("--------3 Using Functions        ----------")


def get_max_char(str1):
    a = 256
    ctr = [0] * a
    m = -1
    ch = ''
    for i in str1:
        ctr[ord(i)] += 1

    for i in str1:
        if m < ctr[ord(i)]:
            m = ctr[ord(i)]
            ch = i
    return ch


print(get_max_char("Python: Get file creation and modification date/times"))
print(get_max_char("abdicate"))



# Python program to return the maximum occurring character in the input string
ASCII_SIZE = 256

def getMaxOccuringChar(str):
	# Create array to keep the count of individual characters
	# Initialize the count array to zero
	count = [0] * ASCII_SIZE

	# Utility variables
	max = -1
	c = ''

	# Traversing through the string and maintaining the count of
	# each character
	for i in str:
		count[ord(i)]+=1;

	for i in str:
		if max < count[ord(i)]:
			max = count[ord(i)]
			c = i

	return c

# Driver program to test the above function
str = "sample string"
print("Max occurring character is",getMaxOccuringChar(str))

# Although this program can be written in atmost 3 lines in Python
# the above program has been written for a better understanding of
# the reader

# Shorter version of the program
# import collections
# str = "sample string"
# print "Max occurring character is " +
#	 collections.Counter(str).most_common(1)[0][0]




def find(myStr):
    # Python program to find the
    # maximum frequency character of the string

    import collections
    # Finding the maximum frequency character of the string
    freq = freq = collections.Counter(myStr)
    maxFreqChar = max(freq, key = freq.get)

    # Printing values
    print("Entered String is ", myStr)
    print(maxFreqChar , "is the maximum frequency character with frequency of " , freq[maxFreqChar])
# Getting string input from the user
myStr = input('Enter the string : ')
find(myStr)



'''



