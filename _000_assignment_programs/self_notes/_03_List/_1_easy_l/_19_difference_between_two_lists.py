'''

# P19. REQ : Difference between 2 lists
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |  +   =    | for if
"""

# 0. Mathematics
"""
1. take two lists
2. use for loop to iterate values present in first list
3. use if condition to check the values present in list1 not in list
4. if it is not there in list2 print that element
5. to store the result take one variable. 3,4 steps stored in variable
6. print result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

list_difference = [element for element in list_1 if element not in list_2]

print(list_difference)

# 2. Algorithm
print("--------2 Algorithm              ----------")

list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

difference_1 = set(list_1).difference(set(list_2))
difference_2 = set(list_2).difference(set(list_1))

list_difference = list(difference_1.union(difference_2))
print(list_difference)

list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

list_difference = []
for element in list_1:
    if element not in list_2:
        list_difference.append(element)

print(list_difference)

# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python code t get difference of two lists
# Using set()
def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


li_1 = [10, 15, 20, 25, 30, 35, 40]
li_2 = [25, 30, 40, 35]
print('List 1 :', li_1)
print('List 2 :', li_2)

print('Difference of list1 and list2 :', Diff(li_1, li_2))

'''


