'''

1. write a program to store  upper and lower case characters of the string separately?

 I. CRUD            :  create
 II. State(variable) :  Datatype/strcuture   str = 'hello everyone be safe'
III. Behavior        :  (Operators,DM,Loops)  +=  for/while

#0 mathematics:

1. Initialize the string
2. take two empty string for lower and upper char store
3. use for loop and separate and add lower and upper char in variables
4. retrieve the required output

# 1. by using inbuilt in functions:

str_1 = 'hello WORld'
print("String : ", str_1)
v = ''
u = ''
for i in str_1:
    if i.islower():
        v += i
    elif i.isupper():
        u += i

print('Lower words string : ', v)
print('Upper words string : ', u)

#2. algorithm:
s="hello WOrld"
print("the string is:",s)
upper=''
lower=''
for i in s:
    if i.islower():
        lower+=i
    elif i.isupper():
        upper+=i
print("lower characters is",lower)
print("upper characters is ",upper)


#3. using functions:

def up_low(string):
  uppers = ''
  lowers = ''
  for char in string:
    if char.islower():
      lowers += char
    elif char.isupper():
      uppers +=char
    else: #I added an extra case for the rest of the chars that aren't lower non upper
      pass
  return(uppers, lowers)

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

'''