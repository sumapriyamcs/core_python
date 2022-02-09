'''
#44.REQ: generate group of five consecutive numbers?

1.CRUD          -------> retrieve

2.STATE          --------->list

3.BEHAVIOUR      --------->  =  /for

#0.mathematics:

1. take a empty list to store the result
2. take a number how many times consecutive numbers wants to print
3. use for loop to iterate number
4. use another for loop  to move forward of elements within range
5. add both for loop values with multiplication of number
6. print result

#1.builtin functions:

l = [[5*i + j for j in range(1,6)] for i in range(5)]
print(l)


#2. algorithm:

n=5
res=[]
for i in range(n):
    for j in range(1,6):
        res=n*i+j
        print(res)

#3. by using functions:

def group(n):

    for i in range(n):
        for j in range(1, 6):
            res = n * i + j
            print(res)
res = []
n = 5
group(n)
'''

