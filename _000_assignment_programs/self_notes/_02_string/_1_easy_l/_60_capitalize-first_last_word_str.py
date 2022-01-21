'''
# P60. REQ : capitalize first and last letters of each word of a given string
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +  =    | for
"""

# 0. Mathematics
"""
str_1 = ' i am hungry '
                ||
                --
expected o/p = ' I AM HungrY'

"""

Step 1:- Start.
Step 2:- Take user input.
Step 3:- Slice string from 0 to 1 and convert its case to uppercase.
Step 4:- Concatenate the string from 1 to length of string – 1.
Step 5:- Concatenate last character after converting it to upper case.
Step 6:- Print the string.
Step 7:- End.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

string = input("Enter a string :-")
new_str = string[0].upper()+string[1:-1]+string[-1].upper()
print(new_str)

# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = 'i am hungry man'
print("String :", str_1)

str_1 = str_1.title()
str_2 = ''
print("String :", str_1)
for i in str_1.split():
    str_2 += i[:-1] + i[-1].upper() + ' '

print('Expected result :', str_2)

#take user input
String = input('Enter the String :')
#start slicing the String
#take 1st character and convert it to upper case
#Concatinate the string with remaning-1 length
#take last character and change it to uppercase and concatinate it to string
String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
#print the String
print(String)

#3.by using functions:

def cap(String):
    #start slicing the String
    #take 1st character and convert it to upper case
    #Concatinate the string with remaning-1 length
    #take last character and change it to uppercase and concatinate it to string
    String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
    #print the String
    print(String)
#take user input
String = input('Enter the String :')
cap(String)

'''
