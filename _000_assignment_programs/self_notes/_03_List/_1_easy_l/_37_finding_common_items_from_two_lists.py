'''
#37. req:finding common items from the two lists?


1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for/if

#0.mthematics:

1. take two lists
2. to remove duplicates values use set data structure
3. to get common values use itersection
4. print result

#1.builtin functions:

list1 = [1, 2]
list2 = [1, 3]

list1_as_set = set(list1)
intersection = list1_as_set.intersection(list2)
#Find common elements of set and list

intersection_as_list = list(intersection)

print(intersection_as_list)

#2. algorithm:

a=[2,9,4,5]
b=[3,5,7,2]
print(set(a).intersection(b))

#3. by using functions:

a=[2,3,4,5]
b=[3,5,7,9]

def common(a,b):
    c = [value for value in a if value in b]
    return c

d=common(a,b)
print(d)
'''
