'''

1. write a program to convert a string into uppercase?

I. CRUD            :  update
II. State(variable) :  Datatype/strcuture   str = 'hello everyone be safe'
III. Behavior        :  (Operators,DM,Loops)   for,>=

#0 mathematics:
1. initialize the string
2. with function upper(), will convert all char in upper case
3. retrieve the output

# 1. by using inbuilt in functions:

str_1 = 'i am an idiot'
print("String            : ", str_1)
print("Upper case String : ", str_1.upper())

#2. algorithm:

# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

print("Original String:")
print(text)

# upper() function to convert
# string to upper_case
print("\nConverted String:")
print(text.upper())


# Python Program to Convert String to Uppercase

string = input("Please Enter your Own String : ")
string1 = ''

for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'):
        string1 = string1 + chr((ord(string[i]) - 32))
    else:
        string1 = string1 + string[i]

print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

#3. using functions:

# Python Program to Convert String to Uppercase
def convert(str_1):
  print("String            : ", str_1)
  print("Upper case String : ", str_1.upper())
str_1 = 'i am employee of mcs'
convert(str_1)



'''

