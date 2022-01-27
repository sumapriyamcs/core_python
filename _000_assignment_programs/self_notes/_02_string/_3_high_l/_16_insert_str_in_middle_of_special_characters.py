'''
# P16. Insert string in middle of special chars
"""
1. CRUD       -->  Update
2. STATE      -->  string
3. BEHAVIOR   -->  int  |    |
"""

# 0. Mathematics
1. take a string
2. find the length of the string, to find use len function with string
3. use one variable to calculate the middle of the string.
4. use len off string with floor division of two
5. print the length of middle index
6.take another varaible to add string in the middle of special characters
7. use middle index with string by using slicing opertion and take adding string
8. print the result

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

str_1="suma $ priya"
print('String length :', len(str_1))
mid = len(str_1) // 2
print("Middle index :", mid)
a_string = str_1[:6] + "suma" + str_1[6:]
#Insert `"suma"` in the middle of `str_1`

print(a_string)
# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = '[[{{(())}}]]'
print("String: ", str_1)
print('String length :', len(str_1))
mid = len(str_1)//2
print("Middle index :", mid)
print("The replace of the String mid with python string is :", str_1[:6] + 'python' + str_1[6:])



s="/*-+!@#*(&^$"
st=input("enter the string to insert")
i=int(input("enter the position where you need to enter"))

st3=""
for j in range(len(s)):
    if j!=i:
        st3=st3+s[j]
        print(st3)
    elif j==i:
        st3=st3+st

print(st3)



#3. by using functions:

def insert(str_1):

    print("String: ", str_1)
    print('String length :', len(str_1))
    mid = len(str_1)//2
    print("Middle index :", mid)
    print("The replace of the String mid with python string is :", str_1[:6] + 'amma' + str_1[6:])
#str_1 = '[[{{(())}}]]'
str_1="/*-+!@#*(&^$"
st=input("enter the string to insert")
i=int(input("enter the position where you need to enter"))
insert(str_1)



def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))


'''
