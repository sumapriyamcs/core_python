'''
# P52. print all permutations with given repetition number of given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =   +=    |   for
"""

# 0. Mathematics
1.import permutations from iteratools
2.use for loop  to check whether permutations are there in permutations are not
with string
3. use join to combine the permutations
4. to store all these use variable
5. print the result

#1. built in functions:


from itertools import permutations
perms = [''.join(p) for p in permutations('ant')]
print(perms)


#2. algorithm:

import itertools

if __name__ == '__main__':
    s = 'ABC'

    nums = list(s)
    permutations = list(itertools.permutations(nums))

    # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    print([''.join(permutation) for permutation in permutations])

#3. by using functions:


# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

# This code is contributed by Bhavya Jain


from itertools import product
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results
print(all_repeat('xyz', 3))
print(all_repeat('xyz', 2))
print(all_repeat('abcd', 4))

'''
