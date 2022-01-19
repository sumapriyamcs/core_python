'''
1) What is Python? What are the benefits of using Python?

-->python is an open source, high level, dynamically typed programming language.
benefits:

-->open source and free

-->easy to learn and the sytax for writing code is also easy

-->high level language which provides easy readability for programmers

-->easy integration as python can easily connect with other languages like c,c++,java etc

-->it supports oop's concept and python inbuilt come with huge libraries which reduces coding lines

-->supports modules and packages concept which help in reusing the code

--------------------------------------------------------------------------------------------------------------------------

2) What is PEP 8?

-->PEP: python enterprise proposal.

-->pep8 is a document which provides the guidelines or standards to be followed
by programmer while writing the python code.

-->like naming convention such function names should be lower case and seperated
two word by underscore and class names with uppercase and do not use underscore.

-->following proper indentation

-->using docstring for commenting multiple lines

-->importing modules in seperate lines and at the top of the file.

-->avoiding unnecessary blank spaces
--------------------------------------------------------------------------------------------------------------------------

3) What is pickling and unpickling?

-->pickling is a process of converting python objects into bytes stream.
it is also called as serializing.

-->unpickling is process of converting bytes stream into python objects.
it is called as deserializing.

-->we use pickle.dump() for pickilng process and pickle.load() for unpickling
process by importing the pickle module
--------------------------------------------------------------------------------------------------------------------------

4) How is Python interpreted?

-->python comes with an intrepreter and huge builtin libraries. the interpreter
consists of compiler and virtual machine.

-->interpreter is a software which runs our python scripts.cpython is a default
interpreter for python which is wriiten in c language and
jython is another popular interpreter which is written in java language.

-->when we execute the source code using python interpreter, the source code is
compiled by compiler which is hidden from programmer,and generates the
byte code(low level) which creates file with extension .pyc and then this .pyc
file will be executed by python virtual machine which converts
into machine level language which can be understand by the os and disolays the o/p.

-->this .pyc file which is created during compilation time will get deleted
once the execution is done.
--------------------------------------------------------------------------------------------------------------------------

5) How is memory managed in Python?

--> the ram memory allocated to python software is divided into two parts
1) stack memory 2) private heap memory.

--> when object is created to store value like a = 10
    then the value 10 is stored in heap memory and variable 'a' is stored in stack memory

--> the variable 'a' holds the address of the value where it is got stored in heap memory

--> so we can say that object 'a' in stack memory is refering to the value stored in heap memory

--> so when we define b = 10 then b object is creating in stack memory which is
pointing or refering to the same address of 10 in heap which a is pointing.

--> when we define a = 20  a is refering to 20 and a holds the address of 10
but when we define same variable with another value like a = 30
then new memory allocation is created for 30 and that address is given to 'a'
and now a is refering to 30 and 20 is deleted by garbage collector.

--> Garbage collector mainly work's on reference count. the count will depends
on number of reference that variable holds such as if one object is refering with
two variables then reference count value of the object is 2. so, garbage collector
work is to delete the object whose reference count is 0 that means
that object is not being used any where in the program.
--------------------------------------------------------------------------------------------------------------------------

6) What are the tools that help to find bugs or perform the static analysis?

--> pychecker and pylint are two tool which helps to find the bugs and analyzing the python code.
--> we can use pychecker by importing pychecker.checker at top of file and in cmd use:
pychecker [options] filename.py
it find the errors like a compiler errors in c,c++
--> pylint is also an open source tool for static code analysis looks for
programming errors and is used for coding standards such as warnings, unwanted spaces etc.
--------------------------------------------------------------------------------------------------------------------------

7) What are Python decorators?

--> python decorators very powerful and useful tool in python since it allows
programmer to modify function or class. it allows us to wrap the another functions
in order to extend the behaviour of wrapped function without permanently modifing it.

--> In Decorators, functions are passed as an argument into another function and
then called inside the wrapper function.
-------------------------------------------------------------------------------------------------------------------------

8) What is the difference between list and tuple?
            list                                                                        tuple
  ------------------------------------------------------------------------------------------------------------------------
--> list is mutable and defined using []                                    --> tuple is immutable an defined using ()
--> it requires more memory                                                 --> it requires less memory
--> it is slower than tuple                                                 --> it is faster than list
--> it comes with more number of built in methods                           --> it comes with lesser built methods than list
--> it is very useful in the case of deletion and insertion etc             --> it is useful in the case of read only operation for accesing the elements.
--------------------------------------------------------------------------------------------------------------------------

9) How are arguments passed by value or by reference?

--> all arguments in python are pass by reference. if we pass immutable arguments
like tuple, int then the passing will act as call by value and if we pass mutable
arguments like list,dictionary then the passing is called as pass by value.

--> generally python uses call by object or sometimes called as call by object reference.
--------------------------------------------------------------------------------------------------------------------------

10) What is Dict and List comprehensions are?

--> list comprehension returns the list values by processing data inside the list
where as dict comprehension is same as like list comprehension which returns
dictionary with key and value pair.

list comprehension for storing square of the value:                           list comprehension for storing square of the value:

x = [1,2,3]                                                                          dic_sq = {i:i*i for i in range(1,11)}
square = [i*i for i in x]                                                            print(dic_sq)
print(square)
o/p: [1,4,9]                                                                         o/p: {1:1,2:4,3:9}
--------------------------------------------------------------------------------------------------------------------------

11) What are built-in type does python provides?

--> none type
--> numeric type --> int, float, complex
--> boolean type --> bool
--> text type  --> str
--> sequence types --> list, tuple, dic
--> set --> set, frozen set
--> binary types --> bytes
-------------------------------------------------------------------------------------------------------------------------

12) Explain namespace in Python

--> name space is basically a system which will control all the names which we
use in our program. it will assure that whatever the names we use is unique
and it won't lead to any conflict i.e (name is a system which will control all
names in program and it will allow us to reuse the name in program.

--> for example each module will have some seperate name space. so,when we
import modules there must be some method or func or etc name would be same
but we can use the method as the uniqueness is provided by name space as namespace
differs from module to module.
--------------------------------------------------------------------------------------------------------------------------

13) What is lambda in Python?

--> lamda is a anonymous function. the lambda function can take any number of
arguments but can have only one expression.
--------------------------------------------------------------------------------------------------------------------------

14) Why lambda forms in python do not have statements?

--> lambda form doesn't have statements as it creates a new function object and
returns that at run time.
--------------------------------------------------------------------------------------------------------------------------

15) Explain pass in Python

--> pass is a statement which performs no operation when it get executes. we use
pass generally to avoid syntax errors.
--------------------------------------------------------------------------------------------------------------------------

16) In Python what are iterators?

--> iterator in python is an object used to iterate iterable objects like list,tuple,dic etc.
--> iterator object is initialized using iter() method and it uses next() method for iteration.
--------------------------------------------------------------------------------------------------------------------------

17) What is the unittest in Python?

--> unit testing is first level of software testing where small testable parts
of the software are tested. this is used to validate the small unit of software is
perforning as designed.unit testing comes under white box testing.
--------------------------------------------------------------------------------------------------------------------------

18) Explain slicing in Python?

--> slicing is a technique which depeds on indexing or index values for accesing
certain range of elements present iterables like list,tuple etc.
    ex: list = [1,2,3,4,5]
        list[startindexnumber : endindexnumber : step]
--------------------------------------------------------------------------------------------------------------------------

19) What are generators in Python?

-->  python generators are functions which returns iterable object and used to create iterators.

--> the generator function is normal function which uses yield keyword instead
of return for returning the value of function.

--> otherwise any function body contains the yield key word then the function
is called as generator function.
--------------------------------------------------------------------------------------------------------------------------
20) What is docstring in Python?

--> a python documentation string is called as docstring which is used for
commenting group of lines , to provide documention of functions, modules, class
about the functionality. the docstring line should begin with capital letter.

--> we can declare docstring with lines you want to comment and we can access
docstring by using doc_ method.
--------------------------------------------------------------------------------------------------------------------------

21) How can you copy an object in Python?

--> in python there are two ways to create copies.1) shallow copy   2) deepcopy
--> shallow copy can done using copy.copy method
--> deep copy can be done using copy.deepcopy method
"""
"""--------------------------------------------------------------------------------------------------------------------------

22) What is negative index in Python?

--> for sequence data types indexing start with 0 firstposition,1 secondposition,...
and negative indexinglike -1 lastposition,-2 last butonepoition ....
--------------------------------------------------------------------------------------------------------------------------

23) How can you convert a number to a string?

--> to convert number to a string we use str() method
-------------------------------------------------------------------------------------------------------------------------

24) What is the difference between xrange and range?

--> the range and xrange are two function that could be used to iterate a certain
number of times in for loop. python 3 doesn't supports the xrange but range function
will behave like xrange in python2. range takes more memory for storing the values
when compared with xrange.
--------------------------------------------------------------------------------------------------------------------------

25) What is module and package in Python?

--> each .py file is called as module and folder consists of this modules and init.py
file are called as packages. these packages can have subpackages also.
--------------------------------------------------------------------------------------------------------------------------

26) What are the rules for local and global variables in Python?

--> when a variable is declared inside the function it is called as local variable
and the scope of local variable is within that function it cannot be used
outside the function.

--> where as variables which are declared outside the function are called as global
variable and scope of global variable is entire program and we can use
 global variable where ever we want and inside function we can use by def variable with global keyword.
--------------------------------------------------------------------------------------------------------------------------

27) How can you share global variables across modules?

--> to share the global variable across the module, create one module with declaring
variable and inporting that module in all modules of app.as you have
imported the module we can share the global variable acrross all modules.
--------------------------------------------------------------------------------------------------------------------------

28) Explain how can you make a Python Script executable on Unix?

--> As the very first line of your file, using the pathname for where the Python
interpreter is installed on your platform.

--> Put #!/usr/bin/env python in the first line of your .py script.

--> Add execution permissions to the file (using chmod).  chmod +x < script.py >

--> Execute the script from command line , eg. by providing ./my_script.py when
in the same directory.
------------------------------------------------------------------------------------------------------------------------

29) Explain how to delete a file in Python?

--> importing os module and by os.remove(filename)
--------------------------------------------------------------------------------------------------------------------------

30) Explain how can you generate random numbers in Python?

--> importing random module and by using random.random() method we can generate
random numbers in python. by default it generates numbers between 0 to 1.
--------------------------------------------------------------------------------------------------------------------------

31) How can you access a module written in Python from C?

--> You can access a module written in Python from C by following method,
--> Module = PyImport_ImportModule(“<modulename>”)
--------------------------------------------------------------------------------------------------------------------------

32) What is the use of // operator in Python?

--> // is a floor division operator which is used for dividing two operands which
gives o/p as number befor decimal numbers like 4//2 ==> 2 not 2.0 as if 4/2 ==> 2.0
--------------------------------------------------------------------------------------------------------------------------

33) Mention five benefits of using Python?

--> python is easy to use and read and learn
--> opensource and community development
--> extensive support libraries
--> presence of third party modules
--> userfriendly datastructures
--------------------------------------------------------------------------------------------------------------------------

34) Mention the use of the split function in Python

--> using split function we can break the string into substring using the seperator
and can return it in the list form.
--------------------------------------------------------------------------------------------------------------------------

35) Explain Flask and its benefits

--> Flask is a web framework. flask allows you to build a web application by
providing tools, libraries and technologies. flask has two dependencies they are:

    Werkzeug a WSGI utility library --> provides libraries
    Jinja2 is a template engine     --> template engine
benefits:
--> Integrated support for unit testing
--> Built-in development server and fast debugger
--> Templating jinja2
--> HTTP request handling function
--> Highly flexible

--------------------------------------------------------------------------------------------------------------------------

36) What is the difference between Django, Pyramid, and Flask?

                   Django                                                                              Flask
    ----------------------------------------------------------------------------------------------------------------------
--> django follows MVT architecture                                          --> Flask follows no architecture
--> django is more extensive than flask                                      --> falsk is less extensive than django
--> easily install using pip                                                 --> can easily install using pip
--> it uses django template                                                  --> it uses jinja2 template
--> django uses django orm for data modeling                                 --> flask doesn't have inbuilt orm but can use any orm from outside like sqlalchemy orm.
--> django more popular framework compared with flask                        --> flask is less popular compared with django
--------------------------------------------------------------------------------------------------------------------------

37) What is Flask-WTF and what are their features?

--> flask-WTF is an extension installed using pip which provides a simple interface
with this WTforms libraries.

--> This is where WTForms, a flexible form, rendering and validation library comes handy

--> Using Flask-WTF, we can define the form fields in our Python script and render
them using an HTML template.

features:
--> Is very secure form as it comes with CSRF token
--> Provides global CSRF protection
--> Provides Integration with web forms
--> Also features Recaptcha supporting
--------------------------------------------------------------------------------------------------------------------------

38) Explain what is the common way for the Flask script to work?

the common way for the flask script to work is:
--> Either it should be the import path for your application
--> Or the path to a Python file
--------------------------------------------------------------------------------------------------------------------------

39) Explain how you can access sessions in Flask?

--> Flask-Session is an extension for Flask that support Server-side Session to your application.

--> The Session is the time between the client logs in to the server and logs out of the server.

--> The data that is required to be saved in the Session is stored in a temporary directory
on the server.

--> The data in the Session stored on the top of cookies and signed by the server cryptographically.

--> Each client will have their own session there own data will be store in their session.
--------------------------------------------------------------------------------------------------------------------------

40) Is Flask an MVC model, and if yes give an example showing MVC pattern for your application?

--> Flask is a minimalistic framework which behaves same as MVC framework.So MVC
is a perfect fit for Flask, and the pattern for MVC we will consider for
the following example

    from flask import Flask
    app = Flask(name)
    @app.route("/")
    Def hello():
    	return "Hello World"
    app.run(debug = True)
--------------------------------------------------------------------------------------------------------------------------
41) Explain database connection in Python Flask?

--> Flask supports database-powered applications (RDBS). Such a system requires
creating a schema, which requires piping the shema.sql file into a sqlite3 command.
So you need to install sqlite3 command in order to create or initiate the database in Flask.

--> Flask allows to request database in three ways

--> before_request(): It is called before a request and pass no arguments

--> after_request(): It is called after a request and pass the response that
will be sent to the client

--> teardown_request(): It is called in a situation when exception is raised, and
response is not guaranteed. They are called after the response has been constructed.
They are not allowed to modify the request, and their values are ignored.

--------------------------------------------------------------------------------------------------------------------------

42) If you have multiple Memcache servers, and one of them fails that contain data,
will it try to get them?

--> The data in the failed server won’t get removed, but there is a provision
for auto-failure, which you can configure for multiple nodes.

--> Fail-over can be triggered during any kind of socket or Memcached server
level errors and not during normal client errors like adding an existing key, etc.

--------------------------------------------------------------------------------------------------------------------------

43) Explain how you can minimize the Memcached server outages in your Python Development?

--> When one instance fails, several of them goes down, this will put a larger
load on the database server when lost data is reloaded as the client make a
request. To avoid this, if your code has been written to minimize cache stampedes,
then it will leave a minimal impact.

--> Another way is to bring up an instance of memcached on a new machine using
the lost machine’s IP address.

--> Code is another option to minimize server outages as it gives you the liberty
to change the Memcached server list with minimal work.

--> Setting timeout value is another option that some Memcached clients implement
for Memcached server outage. When your Memcached server goes down,
the client will keep trying to send a request till the time-out limit is reached.
--------------------------------------------------------------------------------------------------------------------------

44) Explain what is Dogpile effect? How can you prevent this effect?

--> Dogpile effect is referred to the event when cache expires, and websites are
hit by the multiple requests made by the client at the same time. This effect
can be prevented by using a semaphore lock. In this system, when the
value expires, the first process acquires the lock and starts generating a new value.
--------------------------------------------------------------------------------------------------------------------------

45) Explain how memcached should not be used in your Python project?

Here are the ways you should not use memcached in your Python project;
--> Memcached common misuse is to use it as a data store and not as a cache.

--> Never use Memcached as the only source of the information you need to run your
application. Data should always be available through another source as well.

--> Memcached is just a key or value store and cannot perform query over the
data or iterate over the contents to extract information.

--> Memcached does not offer any form of security either in encryption or authentication.
--------------------------------------------------------------------------------------------------------------------------

46) What is Python If Statement?

--> if statements in python are used for decision making.t contains a body of
code that runs only when the condition given in the if statement is true

--> If the condition is false, then the optional else statement runs, which
contains some code for the else condition.

--> When you want to justify one condition while the other condition is not true,
then you use Python if-else statement.
--------------------------------------------------------------------------------------------------------------------------

47) Explain While loop in Python with example

--> While loop does the exact same thing what “if statement” does, but instead
of running the code block once,they jump back to the point where it began the
code and repeat the whole process again.
--------------------------------------------------------------------------------------------------------------------------

48) What is enumerate() in Python?

--> Enumerate() in Python is a built-in function used for assigning an index to
each item of the iterable object. It adds a loop on the iterable objects while keeping
track of the current item and returns the object in an enumerable form. This object
can be used in a for loop to convert it into a list by using list() method.
--------------------------------------------------------------------------------------------------------------------------

49) How can you use for loop to repeat the same statement over and again?

--> You can use for loop for even repeating the same statement over and again.
Here in the example, we have printed out the word “shiva” four times.
    for i in '123u':
    	print ("shiva",i,)
-------------------------------------------------------------------------------------------------------------------------

50) What is Tuple Matching in Python?

--> Tuple Matching in Python is a method of grouping the tuples by matching the
second element in the tuples. It is achieved by using a dictionary by checking
the second element in each tuple in python programming. However, we can make
new tuples by taking portions of existing tuples.
--------------------------------------------------------------------------------------------------------------------------


'''