#string:
'''

1. string is a collection data structure
2. it is immutable because the values present in the string we cannot change
3. we can print the string by using '' "" ''' ''' i.e (single quotes,double quotes, triple quotes)
4. when ever we use more than three lines of statements that time we use doc string i.e (triple quotes).
5. keyword of string is str
6. we can perform  crud operations on string
7.it allows duplicate values/characters
8. it can perform so many builtin methods ex:index,slicing,len etc.
9. we can perform type casting
10. it follows the hash code mechanism(based on ASCII value of each char it will store the data ) to store the data in the memory 

'''
s="modernize"
print(s)
print(type(s))

s="suma"
c='m'
#index
print("the index of the string is :", s[3])
print("position of particular char:",s.index(s))
print("position of particular char:",s.find(c))
print("position of particular char:",s.rfind(c))
print("position of particular char:",s.index(c))
print("position of particular char:",s.rindex(c))

#slicing:
s="priya"
print("the slicing of given string is:",s[0:-1])
print("the slicing of given str:",s[0::-1])

#concatination
s="sai"
p="suma"
a=1
b=2
c=a+b
print(c)
con=s+p
print(con)

#multiplication
s="priya"
g="gopal"
c=(s,g)
print(c*3)

#builtin methods:

s="venu"
print("capitalize the string:",s.capitalize())
s="VENU"
print("casefold string:",s.casefold())
s="VENU"
print("casefold string:",s.lower())

#center
#The center() method will center align the string, using a specified
# character (space is default) as the fill character.

#string
s="suma priya"
p=s.center(20,"*")
print(p)

#*count:
s="pooja"
print(s.count("o"))

s="suma priya suma"
print(s.count("suma"))
#*endswith
print(s.endswith("sai"))
#encode
print(s.encode())
#*find
print(s.find("suma"))

#**format:

t="my name is {s},my emp is {emp}".format(s="suma",emp="12345")
print(t)

s="my name is {m}, my city is {v}". format(m="sathish",v="vijayawada")
print(s)

#*isalpha()

s="sunandha"
print(s.isalpha())

#*isalnum:

s="ravikumar123"
print(s.isalnum())

#*ascii

v="yeswanth12@"
print(v.isascii())

#isdecimal:
s="2345"
print(s.isdecimal())

#*isdigit:

s="143"
print(s.isdigit())

#*islower():

s="priyA"
print(s.islower())

#isnumeric():
s="1234"
print(s.isnumeric())

#*isspace():

v=" "
s=v.isspace()
print(s)

s="software company"
print(s.isspace())
s='\n \n \n'
print(s.isspace())


#istitle():

s="Vijayawada"
print(s.istitle())

#*isupper():
s="NELLORE"
print(s.isupper())

#*join():

s="gudivada "
y="krishna"
x=s+y
z=''.join(x)
print(z)
m="$".join(x)
print(m)

#*lower():
s="madhu"
print(s.islower())

#lstrip() : returns left trim version of string
#syntax:string.lstrip(characters)
#lstrip() method to return a copy of a string with the leading whitespace characters removed:
s='  rojag srinivas'
print(s.lstrip('g rj'))

s = '  Readability counts.'
print(s)
new_s = s.lstrip()
print(new_s)

s = '  Readability counts.'
print(s)
new_s = s.strip()
print(new_s)

s = 'Readability counts.'
print(s)
new_s = s.rstrip()
print(new_s)


#*replace():
s="mcs"
print(s.replace('c','$'))

#rfind():
s="hardeware"
print(s.rfind("e"))

#rindex():
s="brebdy"
print(len(s))
print(s.rindex("d"))

#*rsplit():

s="bujji gvg"
x=s.split()
print(x)

#splitlines():
s="hello how are you where r u \n i am waiting my friend"
x=s.splitlines()
print(x)

#startswith():

s="sadhvik nandhan"
print(s. startswith('s'))

#swapcase():

s="FAMILY LOVE"
print(s.swapcase())

#title():

s="chinna"
print(s.title())

#zfill():
#Fills the string with a specified number of 0 values at the beginning

s="addanki"
x=s.zfill(10)
print(x)