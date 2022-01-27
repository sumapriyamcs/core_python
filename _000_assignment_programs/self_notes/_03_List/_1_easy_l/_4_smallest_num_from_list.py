'''
# P04. REQ : find the smallest number in the list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |    <  =    |for if
"""

# 0. Mathematics:
1. take a list
2. to get min number use min function with taken list
3. print list

#1. built in functons:

t = [1, 2, 3, 4, 5, 6, 7]
print('Given List :', t)
print('Type: ', type(t))

print('Largest value of list :', min(t))


#2. algorithm:

# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[1])



# Python program to find smallest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", *list1[:1])


#3. by using functions:

#smallest element in list

#function
def smallest(list):
    small= list[0]
    for i in list:
        if i<small:
            small=i
    return small

#list
list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
print("smallest in ",list,"is")
print(smallest(list))



def myMin(list1):
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    min = list1[0]

    # Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x < min:
            min = x

    # after complete traversing the list
    # return the "max" value
    return min


# Driver code
list1 = [10, 20, 4, 45, 99]
print("smallest element is:", myMin(list1))


'''



