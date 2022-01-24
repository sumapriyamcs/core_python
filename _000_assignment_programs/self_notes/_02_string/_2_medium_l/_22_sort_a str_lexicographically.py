'''
# P22. REQ :  program to sort a string lexicographically
"""
1. CRUD       -->  update
2. STATE      -->  string
3. BEHAVIOR   -->  int  |     =    | for
"""

# 0. Mathematics
"""
str_1 = 'i am the python 3 engineer'

"""
1. take a string from the user.
2. use sorted function with taken string to print the words present in the string
with alphabetical order.

                (and)
Step 1: Declare a String and store it in a variable.
Step 2: Split the string using split(“ ”) function with space as the parameter
and store all the words in a list.
Step 3: Sort the all the words of list in lexicographical order using sort() function.
Step 4: Use a for loop to iterate over the words in the list and print the word while iterating.
Step 5: End.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
str_1 = 'i am the python 3 engineer'
print("String :", str_1)
print("Lexicographically sorted String :", sorted(str_1))

text='aAaBbcCdE'
print(sorted(text, key=lambda x: (str.lower(x), x)))

#2. algorithm:

my_arr = [
"hello",
"apple",
"actor",
"people",
"dog"
]

print(my_arr)
my_arr.sort()
print(my_arr)

#3. by using functions:

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))


def sortStringInLexo(string):
    words = string.split()
    words.sort()
    for word in words:
        print(word)


#if __name__ == '__main__':
string = "welcome to the world of python programming"
sortStringInLexo(string)

'''



