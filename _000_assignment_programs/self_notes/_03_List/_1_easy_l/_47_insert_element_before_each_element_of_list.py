'''
#47.REQ: insert a element before each element of list?

1.CRUD          ----->CREATE

2. STATE        -----> LIST

3. BEHAVIOUR    ------->   /for 

#  0.mathematics:

1.take a list
2. take empty variable to store the result
3. use for loop to iterate values present in list
4. useanother for loop to add new element of every value before
5. print th result

#1. builtin functions:



#2. algorithm:

color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color = [v for elt in color for v in ('c', elt)]
print("Original List: ",color)


l=[1,2,3,4]
print(l)
for i in l:
    for j in ("suma",i):
        print(j)

#3. by using functions:

def add(color):


    print("Original List: ",color)
    color = [v for elt in color for v in ('saree', elt)]
    print("Original List: ",color)

color = ['Red', 'Green', 'Black']
add(color)

'''


