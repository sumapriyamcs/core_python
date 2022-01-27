'''

# P14. REQ : Remove even elements and print list
"""
1. CRUD       -->  delete
2. STATE      -->  list
3. BEHAVIOR   -->  list  |   %  !=  ==  | for if
"""

# 0. Mathematics
"""
1.Traverse each number in the list by using for...in loop.
2.Check the condition i.e. checks number is divisible by 2 or not – to check EVEN,
number must be divisible by 2.
3.If number is divisible by 2 i.e. EVEN number, remove the number from the list.
4.To remove the number from the list, use list. remove() method.
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")


#Python program to print even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# using list comprehension
odd_nos = [num for num in list1 if num % 2 != 0]

print("Even odd numbers in the list: ", odd_nos)


# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 != 0:
		print(num, end=" ")

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]


# we can also print even no's using lambda exp.
odd_nos = list(filter(lambda x: (x % 2 != 0), list1))

print("odd numbers in the list: ", odd_nos)


# 2. Algorithm

print("--------2 Algorithm              ----------")
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
print('Original List :', list1)
odd_list = []
# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 != 0:
		odd_list.append(num)

print('List after removing even numbers from list1 :', odd_list)



# list with EVEN and ODD number
list = [11, 22, 33, 44, 55]

# print original list
print ("Original list:")
print (list)

# loop to traverse each element in the list
# and, remove elements
# which are EVEN (divisible by 2)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)

# print list after removing EVEN elements
print ("list after removing EVEN numbers:")
print (list)

#3. by using functions:

def remove_even(x):
    for i in x[:]:
        if (i % 2) == 0:
            x.remove(i)
    return x

x = [12, 15, 7, 9,14]
print(remove_even(x))

'''
