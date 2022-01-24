'''
# P25. REQ :  program to create a Caesar encryption
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  int  |   = %  ==    |   for if-elif
"""

# 0. Mathematics
"""
str_1 = ' i am the python engineer '

o/p   = ' k co vjg ravjqp gpikpggt '
"""

1.Define the shift value i.e., the number of positions we want to shift from each character.
2.Iterate over each character of the plain text:
    1.If the character is upper-case:
        1.Calculate the position/index of the character in the 0-25 range.
        2.Perform the positive shift using the modulo operation.
        3.Find the character at the new position.
        4.Replace the current capital letter by this new character.
    2.Else, If the character is not upper-case, keep it with no change.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

str_1 = ' i am the python engineer '
print("String :", str_1)
cipher = ''
shift = 2
for char in str_1:
    if char == ' ':
        cipher = cipher + char
    elif char.isupper():
        cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
        cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

print('Encrypted String :', cipher)

# 2. Algorithm
print("--------2 Algorithm              ----------")

shift = 3  # defining the shift count

text = "HELLO WORLD"

encryption = ""

for c in text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    else:

        # since character is not uppercase, leave it as it is
        encryption += c

print("Plain text:", text)

print("Encrypted text:", encryption)


#by using functions:

#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

#check the above function
text = "ATTACKATONCE"
s = 4
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))



def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher


text = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt(text, s))

'''


