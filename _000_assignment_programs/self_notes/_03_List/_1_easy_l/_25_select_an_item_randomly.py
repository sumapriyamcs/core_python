'''
# P25. REQ : select a random item from a list?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +   |
"""

# 0. Mathematics

1. import random to select random item from the list
2. take one variable to store the result
3.use randchange with len of list to generate the random number with specified length
4. use 3 step with random to print random letter
5. print result

#1. built in functions:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f']
random_index = random.randrange(len(letters))

print(letters[random_index])

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f']
random_index = random.randint(0,len(letters)-1)

print(letters[random_index])


# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,9))


#2. algorithm:

# Python3 code to demonstrate
# to get random number from list
# using random.choice()
import random

# initializing list
test_list = [1, 4, 5, 2, 7]

# printing original list
print ("Original list is : " + str(test_list))

# using random.choice() to
# get a random number
random_num = random.choice(test_list)

# printing random number
print ("Random selected number is : " + str(random_num))

#3. by using builtin functions:


def select(letters):

    import random
    print(random.choice(letters))
letters = ['a', 'b', 'c', 'd', 'e', 'f']
select(letters)

#4. by using oops:

class Generate:
    def __init__(self,letters):
        self.letters=letters
    def num(letters):
        import random
        print(random.choice(letters))
letters = ['a', 'b', 'c', 'd', 'e', 'f']
select=Generate
Generate.num(letters)

'''


