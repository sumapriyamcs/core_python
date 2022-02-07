'''
# P29. REQ : get unique values in list?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for/if
"""

# 0. Mathematics
1. take a list
2. take emply list to store unique values
3. use for loop  to check the values present in the list r not
4. use if condition to check  the values are not present in the empty llist
5. if not present means append the values one by one in empty list
6. print result

#1. by using builtin functions:

mylist = [u'nowplaying', u'PBS', u'PBS', u'nowplaying', u'job', u'debate', u'thenandnow']
unique = list(dict.fromkeys(mylist))
print(unique)



#2. algorithm:

trends=['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']
output = []
for x in trends:
    if x not in output:
        output.append(x)
print(output)

#3.. by using functions:

def get(mylist):
    used = set()
    unique = [x for x in mylist if x not in used and (used.add(x) or True)]
    print(unique)

mylist = [u'nowplaying', u'PBS', u'PBS', u'nowplaying', u'job', u'debate',
              u'thenandnow']
get(mylist)

'''
