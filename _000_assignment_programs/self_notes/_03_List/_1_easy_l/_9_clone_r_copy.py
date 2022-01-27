'''
# P09. REQ :  Clone or copy
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |for
"""

# 0. Mathematics
"""
1. take a list
2.take one variable to store copy of existing list
3. copy the existing list with list data structure(like list(l1))
3. print the result

                (and)

Step 1- Take input of list from user

Step 2- Declare a new list which will be the copy

Step 3- Copy the elements using slicing operator ( : ) in the new list

Step 4- Print the new list which will be the copy of the original list

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


# mixed list
prime_numbers = [2, 3, 5]
print("original list is:",prime_numbers)

# copying a list
numbers = prime_numbers.copy()

print('Copied List:', numbers)



#2. algorithm:

li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = li[:]
print("After cloning: ",list_copy)


li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = []
list_copy.extend(li)
print("After cloning: ",list_copy)

li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = list(li)

print("After cloning: ",list_copy)


li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = [ num for num in li ]

print("After cloning: ",list_copy)

li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = []
for num in li:
    list_copy.append(num)

print("After cloning: ",list_copy)

li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = li.copy()

print("After cloning: ",list_copy)



#3. by using functions:


# Python code to clone or copy a list
# Using the in-built function list()
def Cloning(l1):
    li_copy = list(l1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)



'''
