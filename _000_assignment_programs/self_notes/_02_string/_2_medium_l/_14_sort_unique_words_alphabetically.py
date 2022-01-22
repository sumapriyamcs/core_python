'''
# P014. REQ : Sort unique words alphanumerically
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  str  |    =    |for
"""

# 0. Mathematics
"""
str_1 = 'red 1 black 5 blue 2 green 3 yellow'
exp. o/p = ['1', '2', '3', '5', 'black', 'blue', 'green', 'red', 'yellow']
"""
1. take a string from the user/take string
2. take one variable to store the result
3 .split that string by using split function with taken string
4. use for loop to iterate word present in the string
5.after iterate store the result in variable
6.after that use set to get unique words and use list to convert that wors in
list and sorted that words finally join that words .to get the result use
all these operations in print statement.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

items = input("Input comma separated sequence of words")
words = [word for word in items.split(" ")]
print(" ".join(sorted(list(set(words)))))

str_1 = 'red 1 black 5 blue 2 green 3 yellow'
print("String :", str_1)
print("Sorted String :", sorted(str_1.split()))


# 2. Algorithm
print("--------2 Algorithm              ----------")

items = input("Input comma separated sequence of words")
words = [word for word in items.split(" ")]
print(" ".join(sorted(list(set(words)))))

#by using functions:

def sort(items):
    words = [word for word in items.split(" ")]
    print(" ".join(sorted(list(set(words)))))
items = input("Input comma separated sequence of words")
sort(items)
'''

