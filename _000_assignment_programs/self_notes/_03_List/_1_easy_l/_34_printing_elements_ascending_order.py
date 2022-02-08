'''
#34. req:printing elements in ascending order?
"""
1. CRUD       -->  retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for/if

"""
#0.mathematics:

1. take a list
2. to get the values in ascending order use sort function
3.print results

#1. builtin functions:

numbers = [1, 3, 4, 2]

# Sorting list of Integers in ascending
numbers.sort()

print(numbers)

#2. algorithm:

my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)

print(new_list)

#3. by using functions:


def ascen(Number):
    for i in range(1, Number + 1):
        value = int(input("Please enter the Value of %d Element : " %i))
        NumList.append(value)

    for i in range (Number):
        for j in range(i + 1, Number):
            if(NumList[i] > NumList[j]):
                temp = NumList[i]
                NumList[i] = NumList[j]
                NumList[j] = temp

    print("Element After Sorting List in Ascending Order is : ", NumList)
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
ascen(Number)

'''

