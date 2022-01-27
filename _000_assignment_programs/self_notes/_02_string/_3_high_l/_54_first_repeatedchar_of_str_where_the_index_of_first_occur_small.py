'''
# P54. find the first repeated character of a given string where the index of
first occurrence is
# smallest
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =   +=  >   |   for if/else
"""

# 0. Mathematics:

1. create a function with string
2. take empty set to store result
3. use for loop to iterate chars present in the string
4. use if condition to check if the char in empty set are not
5. if it is present ,return that char and print  index of that chat with string
6. if it is not present store every char in empty set
7. the if condition is not work return none keyword

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

dict = {}
string = "This is a test"
for char in string:
    if char in dict:
        print("First repeated char is '%s'" % char)
        break
    else:
        dict[char] = 1

# 2. Algorithm
print("--------2 Algorithm              ----------")

dict = {}
string = "This is a test"
for char in string:
    if char in dict:
        print("First repeated char is '%s'" % char)
        break
    else:
        dict[char] = 1



string="sumapriya"
#def find_repeater(string):
my_list = []
my_list.append(string[0])
for i in range (1, len(string)):
    if string[i] in my_list:
        print ('repetition found')
        print((string[i]))

    else:
        my_list.append(string[i])

#print (find_repeater('abca'))


# 3 Using Functions
print("--------3 Using Functions        ----------")


def first_repeated_char_smallest_distance(str1):
    temp = {}
    for ch in str1:
        if ch in temp:
            return ch, str1.index(ch)
        else:
            temp[ch] = 0
    return 'None'


print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abcb"))


def rep_char(str1):
    s = str1.lower()
    for index, c in enumerate(s):
        if s[:index + 1].count(c) > 1:
            return c
    return "None"


print(rep_char("Python"))
print(rep_char("EyeHunts"))


def by_value(item):
    return item[1]
dict = {}
string = "This is a test"
first = True
for char in string:
    if char in dict:
        if first:
            print("First repeated char is '%s'" % char)
            first = False
        dict[char] += 1
    else:
        dict[char] = 1
for key, value in sorted(dict.items(), key=by_value, reverse=True):
    if value > 1:
        print("'%s' -> %s" % (key, value))
'''
