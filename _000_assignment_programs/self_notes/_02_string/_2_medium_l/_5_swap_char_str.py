'''
# P05. REQ : Swapping chars in string
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  :: =   |
"""

# 0. Mathematics
"""
str_1 = 'abc dva'

o/p     'avd cba'
"""
1.take a string from the user
2. convert that string into list
3.by using charcter index we swap the characters like zero and one characters
we change like one to zero
4. after changing we join that string by using the join condition within the print statement

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
s = 'badcfe'
print(''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ]))

 # 2. Algorithm:

print("--------2 Algorithm              ----------")

strlst = list("abcdef")
print(strlst)
strlst[0], strlst[1] = strlst[1], strlst[0]
print("".join(strlst))

#3.by using functions:

def solve(s):
   s = list(s)
   for i in range(0, len(s)-1, 2):
      s[i], s[i+1] = s[i+1], s[i]

   return ''.join(s)

s = "programming"
print(solve(s))

'''

