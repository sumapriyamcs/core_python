'''# P01. REQ : count repeated characters in a string

1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =    |


# 0. Mathematics

1. Initialize the string
2. count repeated characters in a string

check_string = "i am checking this string to see how many times each character appears"
                | || ||...............................................................

                5 73 55............................................................... 

# 1.Builtin functions

1. Initialize the string or get string input from user as well as get the characters from the user
2.use for loop to iterate characters.
2. With builtin function count(), will found number of repeat of the substring and
use if condition  to check count of  each characetr greater than one r not
3. if character count greater than one we will print that count of charater

print("--------1 Builtin Functions      ----------")

chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking this string to see how many times each character appears"
print("String :", check_string)
for char in chars:
    count = check_string.count(char)
    if count > 1:
        print(char, count)

#2.algorithm:

import collections
string = "Hello world"
frequencies = collections.Counter(string)
repeated = {}

for key, value in frequencies.items():
#iterate through frequencies dictionary

    if value > 1:
        repeated[key] = value
#if character repeats, add to repeated dictionary


print(repeated)

#3.by using functions:

def char(string):

    import collections
    #string = "Hello world"
    frequencies = collections.Counter(string)
    repeated = {}

    for key, value in frequencies.items():
    #iterate through frequencies dictionary

        if value > 1:
            repeated[key] = value
    #if character repeats, add to repeated dictionary


    print(repeated)
string="hello everyone how are you"
char(string)

'''
