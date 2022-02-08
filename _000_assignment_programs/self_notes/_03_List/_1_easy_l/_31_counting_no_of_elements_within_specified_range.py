'''
# P31. REQ : counting number of elements within specified range?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +=   | for/if
"""

# 0. Mathematics

1. take a list
2.take count variable as a zero to store the result
3. use for loop to check the range of list
4. if the list values are within range store one by one value into count variable
5. print result


#1. by using builtin functions:

l=[1,2,3,4,5]
count=0
for i in range(0,5):
    count+=1
print(count)

#2. algorithm:

# Sample List
lst = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70]
#min = 40
#max = 80
newlist = [x for x in lst ]
print( len(newlist))


#3.by using functions:

list = ['a',1, True, None]
def get_no_of_elements(list):
    count = 0
    for element in range(0,4):
        count += 1
    return count
print("Number of elements in the list: ", get_no_of_elements(list))


def count_range_in_list(li, min, max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))

'''



