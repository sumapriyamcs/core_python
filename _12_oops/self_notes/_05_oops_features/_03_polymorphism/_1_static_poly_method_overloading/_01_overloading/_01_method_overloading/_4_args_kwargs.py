"""

#How we can handle overloaded method requirements in Python:

Most of the times, if method with variable number of arguments required then we can handle
with default arguments or with variable number of argument methods.
"""
#Program with Default Arguments:

class Test:
    def sum(self,a=None,b=None,c=None):
             if a!=None and b!= None and c!= None:
                        print('The Sum of 3 Numbers:',a+b+c)
             elif a!=None and b!= None:
                        print('The Sum of 2 Numbers:',a+b)
             else:
                        print('Please provide 2 or 3 arguments')

t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)

#Program with Variable Number of Arguments::

class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
            print('The Sum:',total)
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()


# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)


# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')


# class
class Compute:
# area method
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
# object
obj = Compute()
# zero argument
print("Area Value:", obj.area())
# one argument
print("Area Value:", obj.area(4))
# two argument
print("Area Value:", obj.area(3, 5))

def addition(a, b):
   return a + b
print(addition(3,4))

def addition(*args):
   result = 0
   for i in args:
      result += i
   return result
print(addition())
print(addition(1,4))
print(addition(1,7,3))

#keyword arguments
def addition(a, b, *args, option=True):
   result = 0
   if option:
      for i in args:
        result += i
      return a + b + result
   else:
      return result

print(addition(1, 4, 5, 6, 7))
print(addition(1, 4, 5, 6, 7, option=False))

#*args and kwargs

def arg_printer(a, b, *args, option=True, **kwargs):
   print(a, b)
   print(args)
   print(option)
   print(kwargs)
arg_printer(1, 4, 6, 5, param1=5, param2=6)
