'''
# P11. REQ :  Find common element from 2 lists
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics

1. take one list
2. take another list
3. to get common elements present in the both lists use intersection
4. to remove duplicate values present in the use set data structure
5.values to be inthe form of list use list
6. use .intersection in the middle of list1 and list2
7. use 3,4,5,6 steps in the print statement to get the results

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]
print(list(set(list1).intersection(list2)))

# 2. Algorithm
print("--------2 Algorithm              ----------")

# Python program to illustrate the intersection
# of two lists using set() method
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
#def intersection(lst1, lst2):
print(list(set(lst1) & set(lst2)))

# Driver Code
#print(intersection(lst1, lst2))

# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python program to find the common elements
# in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if a_set & b_set:
        print(a_set & b_set)
    else:
        print("No common elements")


a_1 = [1, 2, 3, 4, 5]
b_1 = [5, 6, 7, 8, 9]
common_member(a_1, b_1)

a_2 = [1, 2, 3, 4, 5]
b_2 = [6, 7, 8, 9]
common_member(a_2, b_2)

# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3

# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))



# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
	return list(set(lst1) & set(lst2))

# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))

# Python program to illustrate the intersection
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
	return set(lst1).intersection(lst2)

# Driver Code
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))

'''



