'''

# P62. REQ :   compute sum of digits of a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
"""

# 0. Mathematics
"""
1. take a string
2.use varible to store result
3.use for loop to iterate characters
4. use if condition to check whether iterated char in digits are not
5. if it is in digit print that char with int format
6. print that digits sum by using sum function
7. print the result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# python program to compute sum of digits in a string

# take input
string = input("Enter any string: ")

# find sum of digits
sum_digit = sum(int(x) for x in string if x.isdigit())

# display result
print("Sum of digits =", sum_digit)



inputstr = input("Enter your string: ")
sum_total = 0
for x in inputstr:
    if x.isdigit():
        sum_total += int(x)


print("Total:- ", sum_total)





# 2. Algorithm

print("--------2 Algorithm              ----------")
str_1 = 'abs143abd165*&^'
st = []
sum_1 = 0
for i in str_1:
    if i.isdigit():
        st.append(i)
for j in st:
    sum_1 += int(j)

print("String :", str_1)
print('Sum of integer in string is :', sum_1)

#3. by using functions:


def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))

'''

