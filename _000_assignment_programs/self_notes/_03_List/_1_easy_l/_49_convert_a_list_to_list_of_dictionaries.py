'''
#49.REQ: convert a list to list of dictionaries?

1.CRUD          ----->update

2. STATE        -----> LIST

3. BEHAVIOUR    ------->   /for


#0.mathematics:

1. take a values list and keys list
2.use for loop to check values in list or not
3.use another for loop to combine the keys and values
4. to combine use zip function with keys and values
5. use keys and values in the form of dictionary
6. print the result

#1. builtin functions:

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])

#2.algorithm:

t = [[1,2,3], [4,5,6]]
keys = ['a', 'b', 'c']
print([{keys[0]:l[0], keys[1]:l[1], keys[2]:l[2]} for l in t])

t = [[1,2,3], [4,5,6]]
keys = ['a', 'b', 'c']
print([{k:v for k,v in zip(keys, l)} for l in t])

#3.by using functions:


def convert(t,keys):
    d = [dict(zip(keys, l)) for l in t ]
    print(d)

t = [[1,2,3], [4,5,6]]
keys = ['a', 'b', 'c']
convert(t,keys)


#4. by using file handling:

file = open("dataFile.txt", "r")
items = []
for line in file:
    line = map(int,line.split()) #convert the text data to integers
    items.append(line) #add text data to list

'''

