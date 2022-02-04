'''# Tuple:
'''
1. tuple is homogenous and heterogenous data type.
2. it is immutable type. it allows the duplicate values
3. once tuple is created we cannot change the values present in the tuple
4. it maintain the sequence order
5. when compare tolist tuple is too fast
6. it fallows the heap mechanism order for storing the elements in the memory
7. A tuple can be written as the collection of comma-separated (,)
values enclosed with the small () brackets.



#examples:

t=(1,)
print(type(t))
#homogeneous and heterogenous data,duplicates allow
t=(1,1,1.2,"suma",[1,2],{1,2},{"name":"suma","age":24},1.2)
print(t)
print(type(t))
#immutable:
t=(1,2,3)
print(t)

#concatination:
t1=(1,2,3)
t2=(5,6,7)
t=t1+t2
print(t)

#indexing:
t=(1,2,3,4)
print(t[2])
print(t[1])
t1=("dog","cat","mat")
print(t1.index("cat"))

#slicing:
t=(3,4,5,67,3,4,8,9)
print(t[-5:-1])
print(t[::-1])

#all():
t=(1,2,3)
t1=()
print(all(t1))
print(all(t))

#any():

t=(9,8,7,6)
t1=()
print(any(t))
print(any(t1))

t=( 1, 0, 6, 7, False)
print(any(t))

#length():
t=(8,9,7,6,5,4)
print(len(t))

#count:
t=(9,8,7,6,6)
print(t.count(6))

#max() and min():
t1=9
t2=10
t3=11
min=min(t1,t2,t3)
max=max(t1,t2,t3)
print(max)
print(min)

#sum():
t=(8,5,6,7,8)
print(sum(t))

#sorted():
t=(10,11,3,19,0,5,2,1)
print(sorted(t))

'''

#dictionary:
'''
1. it is mutable data structure
2. it contain key value pairs
3.keys must me constant and values can be any type
3. overriding working (i.e, if you give same key with different values
that time last given key value will be printed)
4. it follows unordered structure for storing data
5. it follows hash mechanism
(based on ASCII value of each char it will store the data )

d={"name":"suma","company":"mcs","id": 46,"age":24,"age":30}
print(d)
print(d["age"])
#clear():
d={"name":"suma","company":"mcs","id": 46,"age":24,"age":30}
d.clear()
print(d)

#copy():
d={"name":"sai","company":"testyantra","sal":400000}
print(d)
x=d.copy()
print(x)

#fromkeys():

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)

print(thisdict)

x = ('key1', 'key2', 'key3')
y="mcs"
thisdict = dict.fromkeys(x,y)

print(thisdict)

#get():
d={"name":"sai","company":"testyantra","sal":400000}
print(d["name"])

#items(),keys(),values():
d={"name":"sai","company":"testyantra","sal":400000}
print(d.items())
a=d.items()
b=d.keys()
c=d.values()
print(a)
print(b)
print(c)


#pop():
d={"bike":"bmw","cost":2000000,"model":850}
x=d.pop("model")
print(x)
print(d)

#popitem():
d={"bike":"bmw","cost":2000000,"model":850}
x=d.popitem()
print(x)
print(d)

#setdefault():
d={"bike":"bmw","cost":2000000,"model":850}
x=d.setdefault("bike")
y=d.setdefault("colour","black")
print(x)
print(d)

#update():
d={"bike":"bmw","cost":2000000,"model":850}
#x=d.update({"colour":"white"})
#print(x)
#print(d)
add={"colour":"white"}
d.update(add)
print(d)'''


#set:
'''
1. it is mutable data structure
2. it follows unordered to store the values
3.indexing is not followed in set
4. only immutable data types allowd in set , mutables are not allowed
5. hash mechanism follws for storing the data in memory
'''
#add():

s={1,2,3,4}
s.add("suma")
print(s)

#clear():
s={1,2,2,3,"priya"}
s.clear()
print(s)

#copy():
s={"suma","priya","sai","gopal"}
v=s.copy()
print(v)
print(s)

#difference():
s={"puchalapalli","godavarthi","addanki","yetigadda"}
v={"priya","godavarthi","sai","pooja"}
p=s.difference(v)
print(p)
#difference_update():
'''
the difference_update() method removes the items that exist in both sets.

The difference_update() method is different from the difference() method, because the difference() method returns a new
set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

#discard():

s={3,4,5,8}
s.discard(8)
print(s)

#intersection():
s={9,5,6,7,8}
v={8,3,5,6}
x=s.intersection(v)
print(x)

#intersection update():
'''
The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is
done between more than two sets).
'''
s={9,5,3,4}
v={"sai","bujji",2,9}
s.intersection_update(v)
print(s)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)

#isdisjoint():
'''
The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
'''
s={2,5,6,7}
c={5,7,8,9}
v=s.isdisjoint(c)
print(v)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#issubset():
'''
The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
'''
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#pop():
'''
The pop() method removes a random item from the set.

This method returns the removed item.
'''
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

#remove():
'''
The remove() method removes the specified element from the set.

This method is different from the discard() method, because the remove() method will raise an error if the specified item
does not exist, and the discard() method will not.
'''

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)

#symmetric difference():

x = {"suma", "priya", "sai"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#symmetric_difference_update():
'''
The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and
inserting the other items.

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#union():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "jackfruit"}

z = x.union(y)

print(z)

#update():
''''
The update() method updates the current set, by adding items from another set (or any other iterable).

If an item is present in both sets, only one appearance of this item will be present in the updated set.


'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "goa"}

x.update(y)

print(x)

#list:
'''
1. list is homogeneous and heterogenous data structure
2. it allows duplicates
3.it is little bit slow  compare to tuple
4. it follows heap mechanism to store the data in memeroy

'''