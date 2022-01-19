'''

1. write a program to print the last part of the string?

I. CRUD            :  retrieve
 II. State(variable) :  Datatype/strcuture   str = 'hello everyone be safe'
III. Behavior        :  (Operators,DM,Loops)   list   | = | slice

#0 mathematics:
1. initialize the string
2. separate the string with split function with ' '
3. save split string in new list
4. retrieve the last part of string

# 1. by using inbuilt in functions:

str_1 = 'i am an idiot'
lst = str_1.split(' ')
print("String ", str_1)
print("List ", lst)
print("Last part of string is : ", lst[3])

sample_str = "Sample String"
# Get last 3 character
last part = sample_str[6:]
print('Last part of string: ', last part)

s="helloworld"
print(s)
last=s[5:]
print(last)

#2. algorithm:

sample_str = "Sample String"
# Get last part of string
last part = sample_str[6:]
print('Last part o
_21f string: ', last part)

#3. using functions:

def last_part(s):
  last=s[5:]
  print(last)
s="helloworld"
last_part(s)

'''