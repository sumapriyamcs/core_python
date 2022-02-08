'''
# P30. REQ : get frequency of elements?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for/if
"""

# 0. Mathematics

1.import collections
2. take varible to store the result and use counter of list to count the list
3. with collections use 2nd step and store in variable
4. print result

#1. builtin function:

import collections

myList = [1, 2, 3, 4, 1, 3, 46, 7, 2, 3, 5, 6, 10]
frequencyDict = collections.Counter(myList)
print("Input list is:", myList)
print("Frequency of elements is:")
print(frequencyDict)

#2. algorithm:

# importing the module
import collections

# initializing the list
random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']

# using Counter to find frequency of elements
frequency = collections.Counter(random_list)

# printing the frequency
print(dict(frequency))
{'A': 3, 'B': 3, 'C': 1, 'D': 2}

#by using exception handling:

myList = [1, 2, 3, 4, 1, 3, 46, 7, 2, 3, 5, 6, 10]
frequencyDict = dict()
for element in myList:
    try:
        frequencyDict[element] = frequencyDict[element] + 1
    except KeyError:
        frequencyDict[element] = 1
print("Input list is:", myList)
print("Frequency of elements is:")
print(frequencyDict)

'''
