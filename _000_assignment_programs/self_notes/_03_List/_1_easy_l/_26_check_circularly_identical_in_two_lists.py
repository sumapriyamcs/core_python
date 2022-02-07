'''
# P26. REQ : check circulary identical in two lists?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +   | if/else/for
"""

# 0. Mathematics

#1. by using builtin functions:

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

#2.algorithm:


l1 = [10, 0, 0, 10, 5]

l2 = [10, 5, 10, 0, 0]

l3 = [5, 10, 10, 0, 0]

for i in range(len(l2)):
    l1.append(l1[i])

s1 = str(l1)
s2 = str(l2)
s3 = str(l3)

x = s2[1:len(s2) - 1]
y = s3[1:len(s3) - 1]

print("For l1 and l2 ", x in s1)

print("For l1 and l3 ", y in s1)


list1 = [1, 0, 1, 0, 1]
list2 = [0, 1, 0, 1, 0]

if(' '.join(map(str, list1)) in ' '.join(map(str, list2 * 2))):
    print ("Lists are circularly identical")
else:
    print ("Lists are not circularly identical")


#3. by using functions:

def chain(list1,list2,list3):



    print('Compare list1 and list2')
    print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
    print('Compare list1 and list3')
    print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
chain(list1,list2,list3)

'''
