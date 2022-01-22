'''
# P09. REQ : nth index character from string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |    =    |
"""

# 0. Mathematics
"""
str_1 = 'i am suma and You ?'

exp. o/p  str_1[10] =a
"""
1. take astring from the user
2.to get the index of perticular character from the string use index number of
the string with string.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

str_1 = 'i am suma priya and You ?'
print("String :", str_1)
print("Exp. O/P :", str_1[10])

#algorithm:

st=input("enter the string ")
i=int(input("enter the index"))
st1=""

for j in range(len(st)):
    if j==i:
        st1=st[j]
print(st1[0])

#3.by using functions:


def index(para):


    position1 = (para.find("web"))
    #Above line is used to calculate the position of first "web".
    position2 = (para.find("web"), position1+1)
    #Above line is used to calculate the position of second "web" keyword.
    print (position1)  # print first keyword position
    print (position2)  # print second keyword position

para = "I am web Developer and SEO experts and web based application"
index(para)
'''
