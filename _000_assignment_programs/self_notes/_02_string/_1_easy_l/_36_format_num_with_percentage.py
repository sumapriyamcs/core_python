'''
# P01. REQ : to format a number with a percentage

1. CRUD       -->  Retrieval
2. STATE      -->  Float
3. BEHAVIOR   -->  int  |  =   ,    |


# 0. Mathematics

1. Initialize the number
2. retrieve the number in %
a = 0.25
    25.00%
3. for retrieve we can use format method

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
a_number = 0.20
percentage = "{:.0%}".format(a_number)
print(percentage)

print (str(float(1/3))+'%')

print('{:.1%}'.format(1/3.0))

ratio = round(1/3, 2)
print(f"{ratio} %")

# 2. Algorithm

print("--------2 Algorithm              ----------")

x = 0.25
y = -0.25
z = 0.3456
print("\nOriginal Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x))

print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y))

print("Original Number: ", z)
print("Formatted Number with percentage: "+"{:.2%}".format(z))
z = 0.11111
print("Original Number: ", z)
print("Formatted Number with percentage: "+"{:.2%}".format(z))
print()

val = "The percentage is 95.68"
print("%s%%"%val)

print("95.68%%")

val = "The percentage is 95.68"
print("{}%".format(val))

#by using functions:

def per(x,y,z):

    print("\nOriginal Number: ", x)
    print("Formatted Number with percentage: "+"{:.2%}".format(x))

    print("Original Number: ", y)
    print("Formatted Number with percentage: "+"{:.2%}".format(y))

    print("Original Number: ", z)
    print("Formatted Number with percentage: "+"{:.2%}".format(z))
    z = 0.11111
    print("Original Number: ", z)
    print("Formatted Number with percentage: "+"{:.2%}".format(z))
    print()
x = 0.25
y = -0.25
z = 0.3456
per(x,y,z)

'''

