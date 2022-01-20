'''
# P01. REQ : to print the following floating numbers up to 2 decimal places


1. CRUD       - Retrieve
2. STATE      - Float
3. BEHAVIOR   - =


# 0. Mathematics

1. Define the float number
2. Retrieve up to 2 digit decimal point,to retrieve the two decimal we will use format method .


# 1.Builtin functions :

print("--------1 Builtin Functions      ----------")

float = 2.154327
format_float = "{:.2f}".format(float)
print(format_float)

number = 1.345
f = '{0:.3g}'.format(number)
print(f)

my_float = 2.13456
limit_float = round(my_float, 2)
print(limit_float)


# 2. Algorithm:

print("--------2 Algorithm              ----------")

f = 2.154327

print("Float number :", f)

format_float = "{:.2f}".format(f)

print("Float number with 2 digit decimal point :", format_float)

x = 3.1415926
y = 12.9999
print("\nOriginal Number: ", x)
print("Formatted Number: "+"{:.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number: "+"{:.2f}".format(y));
print()

#3.by using functions:

def deci(float):
    format_float = "{:.2f}".format(float)
    print(format_float)
float=2.154327
deci(float)


'''