'''
# P32. REQ : check if list contain sub list or not?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =  +=   | for/if
"""

# 0. Mathematics

1. take a nested list
2.take sublist
3. use if condition to check sublist is present in original list
4. if it is present print like yes present else not present

#1.by using builtin functions:

list = [[1,5,7,], [2, 3, 4], [3, 6, 9], [4, 8, 12]]
check_list = [2,3,4]
if check_list in list:
	print("List is present")
else:
	print("List is not present")

#2. algorithm:

# Python3 code to demonstrate
# to check if list is subset of other
# using intersection()

# initializing list
test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5]

# printing original lists
print("Original list : " + str(test_list))
print("Original sub list : " + str(sub_list))

# using intersection() to
# check subset of list
flag = 0
if((set(sub_list) & set(test_list)) == set(sub_list)):
	flag = 1

# printing result
if (flag):
	print("Yes, list is subset of other.")
else:
	print("No, list is not subset of other.")


list1=[8,9,7,6]
list2=[7,5,4,3,6]
set1 = set(list1)
#Convert lists to sets

set2 = set(list2)

is_subset = set1.issubset(set2)
#Check if set1 is found in set2

print(is_subset)


#3. by using functions:

def check(list,check_list):

    if check_list in list:
        print("List is present")
    else:
        print("List is not present")

list = [[1,5,7,], [2, 3, 4], [3, 6, 9], [4, 8, 12]]
check_list = [2,3,4]
check(list,check_list)

#4. exception handling:

def sublist(lst1,lst2):
    for item in lst2:
        try:
           lst1.index(item)
        except ValueError:
           return False
    return True

lst1=[1,2,5,6,8,3,2,34,3,4]
lst2=[1,2,3,4]
print(sublist(lst1,lst2))

'''
'''
#Problem Statement:

Consider a positive number innum containing at least two digits, Identify and
print a number outnum based on the logic given below:

Identify all possible rearrangements of the digits of innum such that the
result is a palindromic number

    • Assign the largest palindromic number identified to outnum
    • If no palindrome can be formed, print -1

#Input format:

Read the innum from the standard input stream

#Output format:

Print outnum of -1 accordingly to the standard output stream.

Sample input
2341

Sample Output
-1

Explanation

For the given innum, a
palindrome cannot be
formed by rearranging
the digits, Hence the
output is -1


#solution:

innum=str(input("enter the number"))
print(innum)
import itertools
print(set(itertools.permutations(innum)))
if(innum==innum[::-1]):
      print("The string is a palindrome")
else:
      print(-1)

'''
