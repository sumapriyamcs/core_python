'''
# P21. REQ : list of characters into string?
"""
1. CRUD       -->  update
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     = +=    |for
"""

# 0. Mathematics

1. take a list of characters
2.take one empty varible to store the result
3.to convert that characters into string we use join function with taken list and empty variable
4. print result


#1. builtin functions:

s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
re=''
print(re.join(s))

#2. algorithm:


l=['s','u','m','a']
res=''
for i in l:
    res+=i
    print(res)

#3. by using functions:

# Python program to convert a list
# of character

def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

    # return string
    return new


# driver code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))



# Python program to convert a list
# of character

def convert(s):
    # initialization of string to ""
    str1 = ""

    # using join function join the list s by
    # separating words by str1
    return (str1.join(s))


# driver code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))

'''
'''
hello
HeLlO
'''
