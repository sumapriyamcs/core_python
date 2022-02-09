'''

#51.REQ: split a list every nth element?

1.CRUD          ----->retrieval

2. STATE        -----> LIST

3. BEHAVIOUR    ------->   /for


#0.mathematics:
1. take a list
2. take empty list to store the result
3.take nth number
4.use for loop to iterate the values preset in the list
5.use slicing to split nth element,starting is value and ending is spliting number
6.append one by one value into empty list
7. print result

#1.by using built in functions:


#2. algorithm:

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
s = []
n = 3
for x in range(n):
    s.append(lst[x::n])
    print(s)

#3. by using built in functions:

C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))

'''
