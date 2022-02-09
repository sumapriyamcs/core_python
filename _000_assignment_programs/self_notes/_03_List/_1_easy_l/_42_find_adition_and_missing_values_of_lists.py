'''
#42. req:find the addition and missing values of lists?

1. CRUD       -->  create
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for

#0.mthematics:
1. take a  two lists
2.to find the missing values of two lists use difference of list1 and list2
3. to find the additional values use list2 differene of list1
4. print the results.

#1.builtin functions:

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
print('Additional values in second list: ', ','.join(set(list2).difference(list1)))

#2.algorithm:

# Python program to find the missing
# and additional elements

# examples of lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# prints the missing and additional elements in list2
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))

# prints the missing and additional elements in list1
print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))

#3. by using builtin functions:


def missing(A,B):

    n1=int(input("Enter the size of the First List ::"))
    n2=int(input("Enter the size of the second List ::"))
    print("Enter the Element of first List ::")
    for i in range(int(n1)):
       k=int(input(""))
       A.append(k)
    print("Enter the Element of second List ::")
    for j in range(int(n2)):
       k1=int(input(""))
       B.append(k1)
    # prints the missing and additional elements in first list
    print("Missing values in first list:", (set(B).difference(A)))
    print("Additional values in first list:", (set(A).difference(B)))

    # prints the missing and additional elements in second list
    print("Missing values in second list:", (set(A).difference(B)))
    print("Additional values in second list:", (set(B).difference(A)))

#To find the missing and additional elements
A=list()
B=list()
missing(A,B)

'''

