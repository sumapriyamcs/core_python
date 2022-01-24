'''
# P40. REQ :  reverse words in a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""
1. Initialize the string.
2. Split the string on space and store the resultant list in a variable called words.
3. Reverse the list words using reversed function.
4. Convert the result to list.
5. Join the words using the join function and print it.

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

## initializing the string
string = "I am a python programmer"
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
print(" ".join(words))


# 2. Algorithm
print("--------2 Algorithm              ----------")
str_1 = 'I am suma priya puchalapalli'
print("\nOriginal String : ", str_1)
str_2 = ''
for i in str_1.split(' '):
    str_2 = str_2 + ' ' + i[::-1]
print("Exp. o/p :", str_2)


# Python3 program to reverse a string
# s = input()
s = "i like this program very much"
words = s.split(' ')
string =[]
for word in words:
	string.insert(0, word)

print("Reversed String:")
print(" ".join(string))

#3. by using functions:

# Function to reverse words of string

def rev_sentence(sentence):

	# first split the string into words
	words = sentence.split(' ')

	# then reverse the split string list and join using space
	reverse_sentence = ' '.join(reversed(words))

	# finally return the joined string
	return reverse_sentence

#if __name__ == "__main__":
input = 'geeks quiz practice code'
print (rev_sentence(input))

'''



