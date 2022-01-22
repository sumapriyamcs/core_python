'''
# P06. REQ : Append chars to string at end
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =  +  |
"""

# 0. Mathematics
"""
str_1 = 'abc'

ex. o/p = 'abc cda'
"""
1.take a string from the user
2.take a another string from the user which you want to add at the end
3.take one variable to store the result
4. add both string in that variable which we took before
5. print the result

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
a_str = "Hello"
a_str = a_str[:1] + a_str[1:] +"suma"
print(a_str)

str1 = "Python"
l2 = "G"
res = f"{str1}{l2}"
print(res)

# 2. Algorithm
print("--------2 Algorithm              ----------")

str_1 = 'abc'
print("String :", str_1)
print("Exp. String :", str_1 + ' cba')


st=input("enter the string ")
st1=input("enter what you need to append at the end ")

st3=st+st1
print("the string after appending is  ",st3)

#3. by using functions:

def add(str):
    add_string = " is famous"
    str += add_string
    print("The string is : " + str)
str = "Python"
add(str)
'''
