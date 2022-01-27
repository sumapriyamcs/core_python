'''
# P15. Create html from string
"""
1. CRUD       -->  Create
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  +   |
"""

# 0. Mathematics
1.take a string
2.in which tag you want  to apply for string apply the tag within string
3.use replace menthod to get break of string line
4. store 2 and 3 steps in one variable
5. print the result

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

my_string="hello good morning"
#my_string.replace('\n', '<br>')
html = "<p>" + my_string.replace("\n", "<br>") + "</p>"
print(html)

# 2. Algorithm

print("--------2 Algorithm              ----------")

my_string="hello good morning"
#my_string.replace('\n', '<br>')
html = "<p>" + my_string.replace("\n", "<br>") + "</p>"
print(html)

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))


'''
