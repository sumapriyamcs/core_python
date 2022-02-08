'''
#36.req: variable unique  ientification  number?

1. CRUD              -----> retrieval
2. STATE             ---->list
3. BEHAVIOUR         -------> ==/

#0.mathematics:

1. take a number
2.to convert the number to id use format method with id of taken number
3. print result

#1. builtin functions:

x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x'))

#2.algorithm:

# This program shows various identities
str1 = "geek"
print(id(str1))

str2 = "geek"
print(id(str2))

# This will return True
print(id(str1) == id(str2))

# Use in Lists
list1 = ["aakash", "priya", "abdul"]
print(id(list1[0]))
print(id(list1[2]))

# This returns false
print(id(list1[0])==id(list1[2]))


#3.by using functions:

def con(a,b,c,text):
    print('ID of a =', id(a))
    print('ID of b =', id(b))
    print('ID of c =', id(c))
    print('ID of text =', id(text))
# Python program to illustrate id() function
a = 10
b = 11
c = 130.56
text = 'Hello'
con(a,b,c,text)
'''

