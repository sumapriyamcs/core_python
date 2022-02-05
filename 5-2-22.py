'''

#list:

1. list is homogeneous and heterogenous data structure
2. it allows duplicates
3.it is little bit slow  compare to tuple
4. it follows heap mechanism to store the data in memeroy


l=[1,2,3,"suma","software"]
print(l)

#append():

l=[9,4,6,3]
l.append(95610)
print(l)


a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
print(b)

#clear():

l=["sai","bujji","kannayya","gopal","venu"]
l.clear()
print(l)

#copy():

l=["good","bye","never","talk"]
n=l.copy()
print(n)
print(l)

#count():
l=[1,2,3,4,4,2]
n=l.count(4)
print(n)

#extend():

l=["car","bike","bicycle","flight"]
m=["pen","book"]
l.extend(m)
print(l)
'''
#index():

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)

fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
print(x)

#insert():

flowers=["rose","jasmine","lotus"]
flowers.insert(1,"hybiscus")
print(flowers)

#pop():

l=[1,2.2,"suma","rinky","pooja","madhu"]
l.pop(-1)
print(l)

#remove():

gadgets=["watch","phone","earbuds"]
gadgets.remove("earbuds")
print(gadgets)

#reverse():

dress=["chudidhar","jeans","gagracholi","saree"]
dress.reverse()
print(dress)

#sort():

bags=["college","scholl","office","travel"]
bags.sort()
print(bags)
num=[0,8,1,10,3,2,88]
num.sort()
print(num)