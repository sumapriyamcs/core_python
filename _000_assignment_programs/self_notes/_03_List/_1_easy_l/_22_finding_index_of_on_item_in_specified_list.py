'''
# P22. REQ : finding index of on item in specified list
"""
1. CRUD       -->  retrevial
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics
1. take a string of list/take a list
2. to finding index of an element use index function with specified word /number present in the list
3. print result


#1. builtin functions:

data_types = ["Str", "Int", "Float"]


# Searching for “int”
print(data_types.index("Str"))

#2. algorithm:

num =[10, 30, 4, -6]
print(num.index(30))

#3. by using functions:

def find(lst):

    res = [x for x in range(len(lst)) if lst[x] == 10]

    print ("Indices at which element 10 is present: " + str(res))

lst = [10,20,30,10,50,10,45,10]
print ("List : " ,lst)
find(lst)

'''


