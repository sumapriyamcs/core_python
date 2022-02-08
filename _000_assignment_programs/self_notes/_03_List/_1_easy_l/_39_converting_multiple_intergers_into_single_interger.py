'''
#39. req:converting multiple intergers into single integers?

1. CRUD       -->  retrieve
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for

#0.mthematics:

1. take a list
2.use for loop to iterate the values in the list
3. print results

#1. builtin functions:

L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)

#2. algorithm:

# creating a list
lst = [12, 15, 17]

# iterating each element
for i in lst:
	print(i, end="")

#3. by using functions:

def convert(list1):

    res = int("".join(map(str, list1)))

    return res


list_1 = [1, 2, 3]
print('List :', list_1)
print('Required o/p :', convert(list_1))

'''

