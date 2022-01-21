'''
# P58. REQ : move spaces to the front of a given string
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  ==    | for
"""

# 0. Mathematics
"""
str_1 = ' i am h un gry ! '
                ||
                --
expected o/p = '       iamhungry'

"""


1. Initialise the string.
2. Find out all the characters which are not spaces and store them in a variable.
3. Find out the no. of spaces by count method of the string.
4. Multiply a space by no. of spaces and store it in a variable.
5. Append all the characters to the previous variable.
6. Print the result at the end.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

## initializing the string
string = "tutorials point "

## finding all character exclusing spaces
chars = [char for char in string if char != " "]
## getting number of spaces using count method
spaces_count = string.count(' ')
## multiplying the space with spaces_count to get all the spaces at front of the new_string
new_string = " " * spaces_count
## appending characters to the new_string
new_string += "".join(chars)
## priting the new_string
print(new_string)



# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = ' i am h un gry ! '
print("String with space :", str_1)
count = 0
for i in str_1:
    if i == ' ':
        count += 1
str_2 = ' '*5 + str_1.replace(' ', '')
print("String with space move on front :", str_2)



## initializing the string
string = "tutorials point "
## finding all character exclusing spaces
chars = [char for char in string if char != " "]
## getting number of spaces using count method
spaces_count = string.count(' ')
## multiplying the space with spaces_count to get all the spaces at front of the ne
w_string
new_string = " " * spaces_count
## appending characters to the new_string
new_string += "".join(chars)
## priting the new_string
print(new_string)

#3.by using algorithm:

def space(string):

    ## finding all character exclusing spaces
    chars = [char for char in string if char != " "]
    ## getting number of spaces using count method
    spaces_count = string.count(' ')
    ## multiplying the space with spaces_count to get all the spaces at front of the new_string
    new_string = " " * spaces_count
    ## appending characters to the new_string
    new_string += "".join(chars)
    ## priting the new_string
    print(new_string)

## initializing the string
string = "tutorials point "
space(string)

'''

