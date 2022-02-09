'''
#50.REQ: sort list of nested dictionary?

1.CRUD          ----->retrieval

2. STATE        -----> LIST

3. BEHAVIOUR    ------->   /for


#0.mathematics:

#1. by using builtin functions:

my_collection = {
   'KEY1':{'name':'foo','data':1351,'completed':100},
   'KEY2':{'name':'bar','data':1541,'completed':12},
   'KEY3':{'name':'baz','data':58413,'completed':18}
}
sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x]['completed']))
print(sorted_keys)


#2.algorithm:

my_list = [{'key': {'sub key': 1}}, {'key': {'sub key': 10}}, {'key': {'sub key': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['sub key'], reverse=True)
print("Sorted List: ")
print(my_list)

#3. by using functions:

def sort(my_collection):

    sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x]['completed']))
    print(sorted_keys)

my_collection = {
   'KEY1':{'name':'foo','data':1351,'completed':100},
   'KEY2':{'name':'bar','data':1541,'completed':12},
   'KEY3':{'name':'baz','data':58413,'completed':18}
}
sort(my_collection)

'''
