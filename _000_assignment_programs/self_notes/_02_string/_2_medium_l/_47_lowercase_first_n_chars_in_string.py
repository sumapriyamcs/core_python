'''
# P47. REQ :  lowercase first n characters in a string
"""
1. CRUD       -->  update
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
"""

# 0. Mathematics
"""
1. take a string
2.use slicing operation from which char to  which char you will convert into lowercase
3. to string we use slicing operation  with .lower function
4. both starting and ending characters numbers or index we will mention
5. within print statement we use 2,3,4 steps to get the results


"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
str1 = 'I AM NOT JOKER'
print(str1[:7].lower() + str1[7:])



#2. algorithm:

str1 = 'W3RESOURCE.COM'
print(str1[:4].lower() + str1[4:])

#3. by using functions:

def decapitalize(str):
    return str[:3].lower() + str[3:]

print( decapitalize('HELlo') )


'''


