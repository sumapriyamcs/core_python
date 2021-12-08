'''Python decorators come in 2 related flavors.

1.Function Decorators: A reference to a function is passed to decorator and the decorator returns a modified function.
The modified functions contain references and calls to the original function.

2.Class Decorators: A reference to a class is passed to a decorator and the decorator returns a modified class.
The modified classes contain references and calls to the original class.

#First Class functions in Python:?
First


class objects in a language are handled uniformly throughout.They may be stored in data structures, passed as arguments,
or used in control structures.A programming language is said to support
first- class functions if it treats functions as first- class objects.Python supports the concept of First Class functions.

#Properties of first class functions::?

1.A function is an instance of the Object type.
2.You can store the function in a variable.
3.You can pass the function as a parameter to another function.
4.You can return the function from a function.
5.You can store them in data structures such as hash tables, lists, …

1. Functions are objects: Python functions are first class objects. In the example below,
we are assigning function to a variable. This assignment doesn’t call the function.
It takes the function object referenced by shout and creates a second name pointing to it, yell.

'''
# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()

print (shout('Hello'))

yell = shout

print (yell('Hello'))
'''
2. Functions can be passed as arguments to other functions:
Because functions are objects we can pass them as arguments to other functions.
Functions that can accept other functions as arguments are also called higher-order functions.
In the example below, we have created a function greet which takes a function as an argument.'''

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function
					passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)
'''
3. Functions can return another function: Because functions are objects we can return a function from another function.
In the below example, the create_adder function returns adder function.'''

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print (add_15(10))


