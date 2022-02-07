'''
# P27. REQ :  finding second smallest num in list?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +   | if/else/for
"""

# 0. Mathematics


1.Take in the number of elements and store it in a variable.
2.Take in the elements of the list one by one.
3.Sort the list in ascending order.
4.Print the last element of the list.
5.Exit.


#Program Explanation:

1.User must enter the number of elements and store it in a variable.
2.User must then enter the elements of the list one by one using a for loop and store it in a list.
3.The list should then be sorted.
4.Then the first element of the list is printed which is also the smallest element of the list.

#1. builtin functions:

import math
arr = [10, 13, 17, 11, 34, 21]
arr.sort();
print(arr[1])

#2. algorithm:

li = []
n = int(input("Enter the number of elements: "))
for i in range(1, n+1):
    elem = int(input("Enter the elements: "))
    li.append(elem)
li.sort()

print("The sorted list: ", li)
print("The second smallest value of this list: ",li[1])


#3. by using functions:

# Python prog to illustrate the following in a list
def find_len(list1):
	length = len(list1)
	list1.sort()
	print("Largest element is:", list1[length-1])
	print("Smallest element is:", list1[0])
	print("Second Largest element is:", list1[length-2])
	print("Second Smallest element is:", list1[1])

# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)



def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, 3, 4]))


'''
