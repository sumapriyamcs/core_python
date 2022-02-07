'''
# P28. REQ :  finding second largest num in list?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +   | for
"""

# 0. Mathematics

1. take a list
2. to get the  order of the elements in the list use sort function
3.after sort use negative index to get second most largest element from the list
4. print the list

#1. builtin functions:

# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the second last element
print("Second largest element is:", list1[-2])

#2. algorithm:

# Python program to find second largest
# number in a list

# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)


# print second maximum element using sorted() method
print("Second largest element is:", sorted(list1)[-2])


#3. by using functions:

def find(list1):



    # new_list is a set of list1
    new_list = set(list1)

    # removing the largest element from temp list
    new_list.remove(max(new_list))

    # elements in original list are not changed
    # print(list1)

    print(max(new_list))

# list of numbers
list1 = [10, 20, 4, 45, 99]
find(list1)

'''

