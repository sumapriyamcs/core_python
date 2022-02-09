'''
#43.REQ: split list into different variables?

1.CRUD          -------> retrieve

2.STATE          --------->list

3.BEHAVIOUR      --------->  =  /for

#0.mathematics:

1. take a list of strings with comma sepataed
2. store  a list in different variables
3. print each variable separately

#1. builtin functions:

# Split a Python List into Chunks using For Loops
our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
chunked_list = list()
chunk_size = 3
for i in range(0, len(our_list), chunk_size):
    chunked_list.append(our_list[i:i+chunk_size])
print(chunked_list)

#2. algorithm:


color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)



#3. by using functions:

def split(color):


    var1, var2, var3 = color
    print(var1)
    print(var2)
    print(var3)

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
split(color)


'''
