'''
# P23. REQ : flatten a shallow to list?
"""
1. CRUD       -->  retrevial
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |for
"""

# 0. Mathematics

1. take a nested list
2. import itertools
3. take empty variable to store the result
4.to combine nested lists within one list use chain method with taken list
5. after that,use itertools with 4 step
6. to convert that data with list use list to 4 and 5 steps
7.  4,5,6 store in variale and print result

#1. by using builtin functions:

lst  =[[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
import itertools
flatlist = list(itertools.chain(*lst))
print(flatlist)

#2. algorithm:

lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
flatlist = []
for sublist in lst:
   for item in sublist:
      flatlist.append(item)
print (flatlist)

#3. by using functions:

def find(original_list):

    import itertools
    new_merged_list = list(itertools.chain(*original_list))
    print(new_merged_list)
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
find(original_list)

'''

