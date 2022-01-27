'''
# P07. REQ : remove duplicates from the list
"""
1. CRUD       -->  delete
2. STATE      -->  list
3. BEHAVIOR   -->  list  |    <  =  +  |for if
"""

# 0. Mathematics:

1. take a list
2. to remove duplicates use set data structure with taken list
3. print result

#1. built in functions:

my_list = [1,1,2,3,2,2,4,5,6,2,1]
my_final_list = set(my_list)
print(list(my_final_list))

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

#2. algorithm:

lst = [10, 1, 5, 3, 1, 11, 19, 10, 11]
print('Given List :', lst)
print('Type: ', type(lst))
st = set(lst)

print('List without duplicate element :', list(st))



# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using naive method
# to remove duplicated
# from list
res = []
for i in test_list:
	if i not in res:
		res.append(i)

# printing list after removal
print ("The list after removing duplicates : " + str(res))

#initializing the list
list_value1=[12,15,11,12,8,15,3,3]
print("The initialized list is ",list_value1)
res_list=[]
#using list comprehension
[res_list.append(i) for i in list_value1 if i not in res_list]
#printing the list after removing duplicate elements
print("The resultant list after removing duplicates is ",res_list)

#initializing the list
list_value1 = [12,15,11,12,8,15,3,3]
print("The initialized list is ",list_value1)
res_list = [x for n,x in enumerate(list_value1) if x not in list_value1[:n]]
#printing the list after removing duplicate elements
print("The resultant list after removing duplicates is ",res_list)

from collections import OrderedDict
#initializing the list
list_value1 = [12,15,11,12,8,15,3,3]
print("The initialized list is ",list_value1)
#using OrderedDict
res_list = list(OrderedDict.fromkeys(list_value1))
#printing the list after removing duplicate elements
print("The resultant list after removing duplicates is ",res_list)

#3. by using functions:

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

'''
