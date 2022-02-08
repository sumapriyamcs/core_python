'''
#33.req. generate all sublists in list?

"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for
"""

# 0. Mathematics

Step 1 : given a list.
Step 2 : take one sublist which is empty initially.
Step 3 : use one for loop till length of the given list.
Step 4 : Run a loop from i+1 to length of the list to get all the sub arrays from i to its right.
Step 5 : Slice the sub array from i to j.
Step 6 : Append it to an another list to store it.
Step 7 : Print it at the end.

#1. builtin functions:

l = [1, 2, 3]
lists = [[]]
for i in range(len(l) + 1):
    for j in range(i):
            lists.append(l[j: i])
    print(lists)

#2.algorithm:

data=[1,2,3]
sublists = [[]]
for   length    in  range (1,  len (data) + 1):
      # Generate the sublists starting at each index
    for   i  in  range (0,  len (data)    - length + 1):
         # Add the current sublist to the list of sublists
         sublists.append(data[i   : i  + length])

# Return the result
print(sublists)

#3. by using functions:

# Python program to print all
# sublist from a given list
# function to generate all the sub lists
def displaysublist(A):
   # store all the sublists
   B = [[ ]]

   # first loop
   for i in range(len(A) + 1):
      # second loop
      for j in range(i + 1, len(A) + 1):
         # slice the subarray
         sub = A[i:j]
         B.append(sub)
   return B

# driver code
A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
print("SUBLIST IS ::>",displaysublist(A))

'''
