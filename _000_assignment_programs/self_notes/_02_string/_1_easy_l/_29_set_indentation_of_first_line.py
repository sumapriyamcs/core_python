
'''
# P01. REQ : to set the indentation of the first line


1. CRUD       - Retrieve
2. STATE      - String
3. BEHAVIOR   - str


"""
Indentation in Python refers to the (spaces and tabs) that are used at the beginning of a statement.
The statements with the same indentation belong to the same group called a suite.
"""
# 0. Mathematics

1. Initialize a string
2. retrieve the string with new line


# 1.Builtin functions

print("--------1 Builtin Functions      ----------")


msg = 'Good mood bad mood'
print("String : ", msg)
print('String length :', len(msg))
print('String before indentation of first line:', msg.center(18, '\n'))

print('String after indentation of first line :', msg.center(19, '\n'))

# 2. Algorithm

print("--------2 Algorithm              ----------")
import textwrap
sample_text = ''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 = textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()

j = 1
while(j<= 5):
    print(j)
j = j + 1

#3.by using functions

def f(site):

  if site == 'edu':
     print('Logging in to EduCBA!')
  else:
    print('Please type the URL again.')
    print('You are ready to go!')
site = 'edu'
f(site)

