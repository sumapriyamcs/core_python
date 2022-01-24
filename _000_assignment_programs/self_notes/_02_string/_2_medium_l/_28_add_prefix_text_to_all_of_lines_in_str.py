# P28. REQ :  to add a prefix text to all of the lines in a string
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""
1. take a string
2. take one variable to store the result
3. split the taken string with split function
4.use for loop to iterate the characters present in th string
5.to add prefix of each line ,before printing the character we use > symbol with 
in string in print statement

"""


# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

pera='''Hey i am a kishita.Now days i am doing tarining in AI and Machine learning.I am doing training from Goeduhub'''

list1=pera.split('.')

for i in list1:

    print(">"+i)

#2.algorithm:

str_1 = """ Hey i am a Wichita.Now days i am doing training in AI and Machine learning.I am doing training 
from Github. If you want to join then you are welcome."""
import textwrap
sample_text = """ Hey i am a Ali.Now days i am doing training in AI and Machine learning.I am doing training 
from Github. If you want to join then you are welcome."""
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)

# wrapped += '\n\nSecond paragraph after a blank line.'
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()


#3. by using functions:

def pre(s):

        # Python3 code to demonstrate working of
        # Append suffix / prefix to strings in list
        # Using list comprehension + "+" operator

    # initializing append_str
    append_str = 'gfg'

    # Append suffix / prefix to strings in list
    pre_res = [append_str + sub for sub in s]
    suf_res = [sub + append_str for sub in s]
    pre_res1 = [append_str+s]
    suf_res2=[append_str+s]
    # Printing result
    print("string after prefix addition : " + str(pre_res))
    print("string after suffix addition : " + str(suf_res))
    print(pre_res1)
    print(suf_res2)

# initializing list
test_list = ['a', 'b', 'c', 'd']
print(test_list)
s="suma"
print(s)
# printing list
print("The original list : " + str(test_list))
#print string
print("The original string : " +(s))
pre(s)