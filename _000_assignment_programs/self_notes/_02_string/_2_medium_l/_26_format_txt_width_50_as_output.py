'''
# P26. REQ :  display formatted text (width=50) as output

1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |     =    |

'''
# 0. Mathematics

'''
1. import textwrap
2. take a long string
3. use how much width you want to use
4.use fill function to get the proper output with width
5. use textwrap. with fill function
6. to get the output use 3&4&5 steps within print statement
'''

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

import textwrap
s="hello world good morning how are you all everything is okay happy new year evryone"
print(s)
print(textwrap.fill(s, width=50))

#2. algorithm:
"""
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()
"""
#3.by using functions:
"""
def format(sample_text):

    import textwrap
    print()
    print(textwrap.fill(sample_text, width=50))
    print()
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
format(sample_text)
"""
