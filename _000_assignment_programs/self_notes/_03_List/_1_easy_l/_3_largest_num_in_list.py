'''
# P03. REQ : find the largest number in the list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |    >  =    |
"""

# 0. Mathematics:
1. take a list
2. to get max number use max function with taken list
3. print list

#1. built in functons:

t = [1, 2, 3, 4, 5, 6, 7]
print('Given List :', t)
print('Type: ', type(t))

print('Largest value of list :', max(t))


#2. algorithm:

# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[-1])

#3. by using functions:

# Python program to find largest
# number in a list

def myMax(list1):
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]

    # Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x > max:
            max = x

    # after complete traversing the list
    # return the "max" value
    return max


# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))


'''



