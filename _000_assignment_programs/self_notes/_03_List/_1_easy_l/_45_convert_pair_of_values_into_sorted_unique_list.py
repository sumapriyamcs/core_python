'''
#45.REQ: convert pair of values into sorted unique list?

1.CRUD          -----> UPDATE

2. STATE        ------> LIST

3. BEHAVIOUR    ------->   /


#0. mathematics:

1. take a list with duplicate values
2. to get the unique values use set data structure and to get the values in order way use sorted
function with set
3. to get the  values from the list use union with  star of list
4. print result

#1. builtin functions:

input_list = [(196, 128), (196, 128), (196, 128), (128, 196),
(196, 128), (128, 196), (128, 196), (196, 128),
(128, 196), (128, 196)]
print(sorted(set().union(*input_list)))

#2. algorithm:

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))


#3. by using functions:

lst1 = [(13, 2), (3, 34), (14, 23), (85, 62), (37, 8), (81, 2), (63, 24), (23, 84)]

def unique_lst(l1):
    s1 = set(set().union(*l1))
    s_sorted = sorted(s1)
    return s_sorted

print(f'Sorted single list - {unique_lst(lst1)}')



'''



