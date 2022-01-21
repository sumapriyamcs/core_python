'''

# P48. REQ : swap comma and dot in a string
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  ==  =    | for
"""

# 0. Mathematics
1. take input from the user
2.take empty list to store the result
3.use for loop to iterate each character present in the list
4. use if condition to check whether the i variable equal to dot append the comma in that place
5.use iflese if i variable equal to comma then append the dot in that place by using append method
6.use else whenever above both conditions are not satisfy ,and add variable in list
7. join the m with all replacement in print statement

"""
str_1 = '32.567,89'
            ^^
            ||
str_1 = '32,567.89'

1. Initialize the string
2. Replace comma and dot

"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
str_1 = '32.567,89'
print("String :", str_1)

maketrans = str_1.maketrans
amount = str_1.translate(maketrans(',.', '.,'))
print('String after replace :', amount)

#2.algorithm:

l=input("enter the input:")
m=[]
for i in l:
 if(i=='.'):
  m.append(',')
 elif(i==','):
  m.append('.')
 else:
  m.append(i)
print(''.join(m))

#by using functions:

# Python code to replace, with . and vice-versa
def Replace(str1):
	maketrans = str1.maketrans
	final = str1.translate(maketrans(',.', '.,', ' '))
	return final.replace(',', ", ")


# Driving Code
string = "14, 625, 498.002"
print(Replace(string))

'''
