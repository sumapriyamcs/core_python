'''
# P24. REQ : append a list to second list?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +   |
"""

# 0. Mathematics

1. take two lists
2. use extend method to combine both lists
3. print results

#1. builtin functions:

list1 = [1, 2]
list2 = [3, 4]

list1.extend(list2)
#Combine list1 and list2

print(list1)

#2.algorithm:

list1 = [1, 2]
list2 = [3, 4]

list1.append(list2)
#Add list2 to list1
print(list1)

#3.by using functions:

def add(list1,list2):

    final_list = list1 + list2
    print(final_list)
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
add(list1,list2)

'''
