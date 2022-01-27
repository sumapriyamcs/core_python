'''
# P01. REQ :  sum of list elements
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |    +=  =    |for
"""

# 0. Mathematics
"""
1.take a list
2. take one variable to store result
3. to sum of elemnts of list use sum function with list
4. print result
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
# Python program to find sum of elements in list

# creating a list
list1 = [11, 5, 17, 18, 23]

# using sum() function
total = sum(list1)

# printing total value
print("Sum of all elements in given list: ", total)

# 2. Algorithm
print("--------2 Algorithm              ----------")

t = [1, 2, 3, 4, 5, 6, 7]
print('Given List :', t)
print('Type: ', type(t))
sum_1 = 0
for i in t:
    sum_1 += i
print('Multiply of elements :', sum_1)

# Python program to find sum of elements in list
total = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)

#3. by using functions:

# Python program to find sum of all
# elements in list using recursion
# creating a list
list1 = [11, 5, 17, 18, 23]

# creating sum_list function
def sumOfList(list, size):
    if (size == 0):
	    return 0
    else:
	    return list[size - 1] + sumOfList(list, size - 1)

# Driver code
total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)

'''
