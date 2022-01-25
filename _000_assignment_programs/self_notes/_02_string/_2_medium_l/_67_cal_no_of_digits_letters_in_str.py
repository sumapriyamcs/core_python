'''
# P63. REQ :   that accepts a string and calculate the number of digits and letters
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
"""

# 0. Mathematics
"""
1.Take an input string.

2.While iterating over the whole string, if we find a digit, then increment
the count of digits; otherwise, if we find a letter, then increment the count of letters.

3.Return the count of letters and digits as the output.

                            (and)
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment
the first count variable each time a digit is encountered and increment the
second count variable each time a character is encountered.
4. Print the total count of both the variables.
5. Exit.

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


s = 'some1 string'

numbers = sum(c.isdigit() for c in s)
print(numbers)
letters = sum(c.isalpha() for c in s)
print(letters)
spaces  = sum(c.isspace() for c in s)
print(spaces)
others  = len(s) - numbers - letters - spaces
print(others)



# 2. Algorithm
print("--------2 Algorithm              ----------")
str_1 = input("Enter a string : ")
count_1 = 0
count_2 = 0
count_3 = 0
for i in str_1:
    if i.isdigit():
        count_1 += 1
    elif i.isalpha():
        count_2 += 1
    else:
        count_3 += 1

print("number of digit in your string is :", count_1)
print("number of letter in your string is :", count_2)
print("number of non alphanumeric in your string is :", count_3)


#3. by using functions:
def find(string):
    count1=0
    count2=0
    for i in string:
          if(i.isdigit()):
                count1=count1+1
          count2=count2+1
    print("The number of digits is:")
    print(count1)
    print("The number of characters is:")
    print(count2)
string=input("Enter string:")
find(string)
'''
