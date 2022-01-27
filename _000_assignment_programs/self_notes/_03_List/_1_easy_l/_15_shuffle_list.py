'''
# P15. REQ : Shuffle list and print
"""
1. CRUD       -->  Retrieval/update
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics
"""
1. import random
2. take a list
3. to shuffle list use shuffle function with random
4.print result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
import random

list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ",  list)

random.shuffle(list)
print ("Reshuffled list : ",  list)

# 2. Algorithm
print("--------2 Algorithm              ----------")
# list of numbers
from random import shuffle
list1 = [10, 21, 4, 45, 66, 93]
print('Original List :', list1)

shuffle(list1)
print('Shuffle List :', list1)



#3. by using functions:


import random
def su(list):
    # List after first shuffle
    random.shuffle(list)
    print(list)

    # List after second shuffle
    random.shuffle(list)
    print(list)

list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# Original list
#print(list)
su(list)

'''
