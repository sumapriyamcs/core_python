'''
#41. req:create a multiple list?

1. CRUD       -->  create
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for

#0.mthematics:

1. take a empty list
2. take a number how many times you want to print the lists
3.use for loop to iterate the number
4. append empty list in empty list variable for each iteration
5.print the lists from starting to ending

#1. builtin functions:

lists = []
n = 20
for i in range(n):
    lists.append([])

print (lists[0]) # Prints []
print (lists[19]) # Prints []

#2. algorithm:

obj = {}
for i in range(1, 21):
    obj[str(i)] = []
print(obj)

# Python3 code to demonstrate
# to initialize multiple lists
# using * operator

# using * operator
# to initialize multiple lists
list1, list2, list3, list4 = ([], ) * 4

# printing lists
print ("The initialized lists are : ")
print ("List 1 : " + str(list1))
print ("List 2 : " + str(list2))
print ("List 3 : " + str(list3))
print ("List 4 : " + str(list4))


#3. by using functions:

def mul(n):

    lists = [[] for _ in range(n)]
    print(lists)
n = 5
mul(n)

'''
