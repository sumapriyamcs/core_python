'''
#38. req:change the position of every nth value?

1. CRUD       -->  update
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for

#0.mthematics:

1. take a list
2. use for loop to iterate the items with updation
3.after iterating add one by one value into list
4. print result

#1. builtin functions:

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, len(list1), 2):
    list1[i] +=1
print(list1)

#2.algorithm:


#3. functions:

from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))

'''

