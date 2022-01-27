'''

# P02. REQ :  multiply list elements
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |    *=  =    |for
"""

# 0. Mathematics:
1. to multiply values take product variable
2. take on list
3. use for lop to iterate values present in the list
3. add each value into variable and multiply
4. pint the result

#1. built in function:

# Python3 program to multiply all values in the
# list using lambda function and reduce()
from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]


result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)


product = 1  # Don't use 0 here, otherwise, you'll get zero
             # because anything times zero will be zero.
list = [1, 2, 3]
for x in list:
    product *= x
print(product)


#2.algorithm:

t = [1, 2, 3, 4, 5, 6, 7]
print('Given List :', t)
print('Type: ', type(t))
sum_1 = 1
for i in t:
    sum_1 *= i

print('Multiply of elements :', sum_1)

#3. by using functions:

# Python program to multiply all values in the
# list using traversal

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


'''

