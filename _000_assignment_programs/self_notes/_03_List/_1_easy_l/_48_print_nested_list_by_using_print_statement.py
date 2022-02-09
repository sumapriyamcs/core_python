'''
#48.REQ: Print a nested lists (each list on a new line) using the print() function

1.CRUD          ----->retrieve

2. STATE        -----> LIST

3. BEHAVIOUR    ------->   /for


#0.mathematics:

1. take a nested list
2. use for loop to iterate values present in the list
3. separate each value in new line with \n
4. convert that list to string and join each value
5.print results

#1. built in functions:

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

#2.algorithm:

A = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
[print(a) for a in A];

A = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
[print(*a) for a in A];

# code
list = [10, 20, 30, 40, [80, 60, 70]]

# Printing sublist at index 4
print(list[4])

# Printing 1st element of the sublist
print(list[4][0])

# Printing 2nd element of the sublist
print(list[4][1])

# Printing 3rd element of the sublist
print(list[4][2])



my_list = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]

for item in my_list:
        for x in item:
            print (x)
        print ()


A = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]

for i in A:
        print(*i)

#3. by using functions:


def nested(list):



    # looping through nested list using indexes
    for names in list:
        print(names[0], "is", names[1],
            "years old.")
list = [["Rohan", 60], ["Aviral", 21],
		["Harsh", 30], ["Rahul", 40],
		["Raj", 20]]
nested(list)


#4. by using generators:

lst = [[1, 3, 4], [2, 5, 7]]

def f(lst ):
    yield from lst


for x in f(lst):
    print(*x)

'''


