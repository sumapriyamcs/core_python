'''
# P01. REQ : to count occurrences of a substring in a string?
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =    |
"""

# 0. Mathematics
"""
1. Initialize the string
2.take substring from the string
3.for count the occurences of substring take one builtin count function
4.after counting the occurrences of substring with string ,result stroed in count function
5.then ,print the count function
"""

# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2. With builtin function count(), will found number of repeat of the substring
and Retrieve the count() value
"""
print("--------1 Builtin Functions      ----------")
a = 'caatatab'
b = 'ata'
print(a.count(b)) #overlapping

string = "abracadabra"
substring = "bra"
ct = string.count(substring)
print("Count:",ct)

#2.algorithm:

#defining string and substring
str1 = "This dress looks good; you have good taste in clothes."
substr = "good"

#occurrence of word 'good' in whole string
count1 = str1.count(substr)
print(count1)

#occurrence of word 'good' from index 0 to 25
count2 = str1.count(substr,0,25)
print(count2)


# defining string
str1 = "This dress looks good; you have good taste in clothes."

# defining substring
substr = "good"

# printing original string
print("The original string is : " + str1)

# printing substring
print("The substring to find : " + substr)

# using list comprehension + startswith()
# All occurrences of substring in string
res = [i for i in range(len(str1)) if str1.startswith(substr, i)]

# printing result
print("The start indices of the substrings are : " + str(res))

#3. by using functions:

def sub(ini_str,sub):

    # Count count of substrings using startswith
    res = sum(1 for i in range(len(ini_str))
            if ini_str.startswith("aba", i))

    # Printing result
    print("Number of substrings", res)
# Python code to demonstrate
# to count total number
# of substring in string

# Initialising string
ini_str = "ababababa"
sub_str = 'aba'

sub(ini_str,sub_str)



def find(str1,substr):
    # printing original string
    print("The original string is : " + str1)

    # printing substring
    print("The substring to find : " + substr)

    # using list comprehension + startswith()
    # All occurrences of substring in string
    res = [i for i in range(len(str1)) if str1.startswith(substr, i)]

    # printing result
    print("The start indices of the substrings are : " + str(res))

# defining string
str1 = "This dress looks good; you have good taste in clothes."

# defining substring
substr = "good"
find(str1,substr)

'''
