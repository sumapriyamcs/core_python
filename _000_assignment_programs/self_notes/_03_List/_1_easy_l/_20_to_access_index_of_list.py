'''
# P20. REQ : To access index of list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |if else
"""

# 0. Mathematics
"""
1. take a list
2. to store the result take one variable
3.to get the index of particular value use index function with particular
value or word from the list
4. print result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

animals = ['cat', 'dog', 'rabbit', 'horse']
# get the index of 'dog'
index = animals.index('dog')
print(index)


# 2. Algorithm
print("--------2 Algorithm              ----------")
# Python3 program for demonstration
# of list index() method

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print the index of '4' in list1
print(list1.index(4))

list2 = ['cat', 'bat', 'mat', 'cat', 'pet']

# Will print the index of 'cat' in list2
print(list2.index('cat'))


# 3 Using Functions
print("--------3 Using Functions        ----------")

# Python3 code to demonstrate
# to get index and value
# using naive method

# initializing list
test_list = [1, 4, 5, 6, 7]

# Printing list
print("Original list is : " + str(test_list))

# using naive method to
# get index and value
print("List index-value are : ")
for i in range(len(test_list)):
    print(i, end=" ")
    print(test_list[i])

#3. by using functions:

def find(cities):
    if city in cities:
        result = cities.index(city)
        print(f"The {city} has an index of {result}.")
    else:
        print(f"{city} doesn't exist in the list.")

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'New York'
find(cities)

'''




