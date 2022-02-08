'''
#35. req:creating a list by concatinating a given list which range goes from 1 to n?

"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for

"""
#0. mathematics:

1. take a list
2. take a number for how many timethe list should print
3. take one empty variable to store the result
4. use for loop check the range of list
5. if it is within range print the values one by one
6.print the result

#1. builtin functions:

my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)


#2. algorithm:

list2 = [1,2]
n = 5

list1 = [list2 for x in range(0,n)]

print(list1)

#3. by using builtin functions

def con(list2):
    list1 = [list2 for x in range(0,n)]
    print(list1)
list2 = [1,2]
n = 5
con(list2)


'''

