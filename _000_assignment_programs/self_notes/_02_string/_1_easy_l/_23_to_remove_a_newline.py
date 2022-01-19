'''

1. write a program to remove a newline in a string?

I. CRUD            :  delete
II. State(variable) :  Datatype/strcuture   str = 'hello everyone be safe\n'
III. Behavior        :  (Operators,DM,Loops)   str,for,list

#0 mathematics:
1. Initialize a string with new line string
2. delete new line and retrieve the string

# 1. by using inbuilt in functions:

str1 = 'Python Exercises\n'
print("String with new line:", str1)
print("String without new line:", str1.rstrip())

str1 = "\n Starbucks has the best coffee \n"
newstr = str1.strip()
print(newstr)


#2. algorithm:

text= "\n Welcome to Python Programming \n"
print(text.strip())

text= "Welcome to Python Programming \n"
print(text.rstrip())

# Python code to remove newline character from string using replace() method

text = "A regular \n expression is a sequence \n of characters\n that specifies a search\n pattern."
print(text.replace('\n', ''))

my_list = ["Python\n", "is\n", "Fun\n"]
new_list = []

print("Original List: ", my_list)

for i in my_list:
    new_list.append(i.replace("\n", ""))
print("After removal of new line ", new_list)

#3. using functions:

def removelines(value):
    return value.rstrip()

mystring = 'This is my string. \n'
print("Actual string:",mystring)
print("After deleting the new line:",removelines(mystring))

def removelines(value):
    return value.replace('\n','')

mystring = 'This is my string \nThis comes in the next line.'
print("Actual string:",mystring)
print("After deleting the new line:",removelines(mystring))


'''

