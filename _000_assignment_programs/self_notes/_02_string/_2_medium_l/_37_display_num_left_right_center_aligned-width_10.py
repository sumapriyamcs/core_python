'''
# P37. REQ :  to display a number in left, right and center aligned of width 10
"""
1. CRUD       -->  Retrieval
2. STATE      -->  Int
3. BEHAVIOR   -->  int  |  < > ^ + :   =    |
"""

# 0. Mathematics
"""
1.take a number
2. convert that number into string
3.if you want to print right side of taken number use rjust function with
width and with converted string number.
4. take a varible to store the result
5. if you want to print left side use ljust and for center use center
6. finally,print the result

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

a_number = 1
number_as_string = str(a_number)
right_aligned_number = number_as_string.rjust(10)
print(right_aligned_number)
leftt_aligned_number = number_as_string.ljust(10)
print(leftt_aligned_number)
center_aligned_number = number_as_string.center(10)
print(center_aligned_number)

# 2. Algorithm
print("--------2 Algorithm              ----------")
x = 22
print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x))
print("Right aligned (width 10)  :"+"{:10d}".format(x))
print("Center aligned (width 10) :"+"{:^10d}".format(x))
print()

# Python3 code to demonstrate
# the working of ljust()

lstr = "I love geeksforgeeks"

# Printing the original string
print ("The original string is : \n", lstr, "\n")

# Printing the left aligned
# string with "-" padding
print ("The left ,right,center aligned strings is : ")
print (lstr.ljust(40, '-'))
print (lstr.rjust(40, '-'))
print (lstr.center(40, '-'))

#3. by using functions:

def align(width,number):

    print (f'{number:>{width}}')
    print (f'{number:<{width}}')
    print (f'{number:^{width}}')
width = 10
number = 123
align(width,number)

'''
'''
# here 20 spaces are reserved for the
# particular output string. And the string
# is printed on the left side
print(f"{'Left Aligned Text' : <10}")
# here 20 spaces are reserved for the
# particular output string. And the string
# is printed on the right side
print(f"{'Right Aligned Text' : >20}")
# here 20 spaces are reserved for the
# particular output string. And the string
# is printed in the middle
print(f"{'Centered' : ^10}")

# assigning strings to the variables
left_alignment = "Left Text"
center_alignment = "Centered Text"
right_alignment = "Right Text"

# printing out aligned text
print(f"{left_alignment : <20}{center_alignment : ^15}{right_alignment : >20}")
# assigning list values to the variables
names = ['Raj', 'Shivam', 'Shreeya', 'Kartik']
marks = [7, 9, 8, 5]
div = ['A', 'A', 'C', 'B']
id = [21, 52, 27, 38]

# printing Aligned Header
print(f"{'Name' : <10}{'Marks' : ^10}{'Division' : ^10}{'ID' : >5}")

# printing values of variables in Aligned manner
for i in range(0, 4):
	print(f"{names[i] : <10}{marks[i] : ^10}{div[i] : ^10}{id[i] : >5}")
'''
