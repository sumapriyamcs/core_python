'''
# P46. REQ : convert a string in a list
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  int  |    =    | list
"""

# 0. Mathematics

"""
str_1 = "abcdxyz"

list_1 = ['a','b','c','d','x','y','z']
"""
# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2.take one list variable to store  the result,With builtin function list(), convert str in list
3.split the given string and store that in list variable already we took
4.print that list

"""
print("--------1 Builtin Functions      ----------")

str_1 = "Hire the top 1% freelance developers"
list_1 = str_1.split()
print(list_1)

#2.algorithm:

str_1 = "abcdxyz"
print("String :", str_1)
print("String to List ", list(str_1))

#given string
string1="Python is great"

#printing the string
print("Actual String: ",string1)

#gives us the type of string1
print("Type of string: ",type(string1))

print("String coverted to list :",string1.split())
#prints the list given by split()

#Given string
string1="This is Python"

print("The actual string:",string1)

#converting string1 into a list of strings
string1=string1.split()

#applying list method to the individual elements of the list string1
list1=list(map(list,string1))

#printing the resultant list of lists
print("Converted to list of character list :\n",list1)

#3.by using functions:

def convert(str_1):

    print("String :", str_1)
    print("String to List ", list(str_1))

str_1 = "abcdxyz"
convert(str_1)


# Python code to convert string to list

def Convert(string):
	li = list(string.split(" "))
	return li

# Driver code
str1 = "Geeks for Geeks"
print(Convert(str1))

# Python code to convert string to list character-wise
def Convert(string):
	list1=[]
	list1[:0]=string
	return list1
# Driver code
str1="ABCD"
print(Convert(str1))

'''
