'''

# P12. REQ : Remove specified index from list and print
"""
1. CRUD       -->  delete
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    | for if
"""

# 0. Mathematics:

1. take a list
2. to remove paticuar index use pop with list
3. print result

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
a = ['a', 'b', 'c', 'd']
a.pop(1)
print(a)

# 2. Algorithm
print("--------2 Algorithm              ----------")

list = [1, 2, 3, 4]
list.remove(1)
print(list)


def delete(mylist):
    #delete item in mylist at index
    mylist.pop(index)

    print(mylist)

mylist = [21, 5, 8, 52, 21, 87, 52]
index = 3
delete(mylist)


# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python3 program to remove the index
# element from the list
# using traversal

def remove(list1, pos):
    new_list = []

    # traverse in the list
    for x in range(len(list1)):

        # if index not equal to pos
        if x != pos:
            new_list.append(list1[x])
    print(*new_list)


list_1 = [10, 20, 30, 40, 50]
pos_1 = 2
remove(list_1, pos_1)
'''

