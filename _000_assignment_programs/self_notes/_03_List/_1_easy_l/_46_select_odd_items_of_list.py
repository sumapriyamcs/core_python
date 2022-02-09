'''
#46.REQ: select odd items of list?

1. CRUD         ------> RETRIEVAL

2. STATE        -------> LIST

3. BEHAVIOUR    -------->   == =! /for/if

#0.mathematics:

1. take a list
2. to print odd numbers use upadation with 2
3. print result

#1. builtin functions:

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[::2])


# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

only_odd = [num for num in list1 if num % 2 == 1]

print(only_odd)

#2. algorithm:


# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 != 0:
        print(num, end=" ")

# Python3 code to demonstrate
# Separating odd and even index elements
# Using list slicing

# initializing list
test_list = [3, 6, 7, 8, 9, 2, 1, 5]

# printing original list
print("The original list : " + str(test_list))

# Using list slicing
# Separating odd and even index elements
res = test_list[::2] + test_list[1::2]

# print result
print("Separated odd and even index list : " + str(res))


#3. by using functions:

def odd(list1):

    # we can also print odd no's using lambda exp.
    odd_nos = list(filter(lambda x: (x % 2 != 0), list1))

    print("Odd numbers in the list: ", odd_nos)
# Python program to print odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]
odd(list1)

'''


