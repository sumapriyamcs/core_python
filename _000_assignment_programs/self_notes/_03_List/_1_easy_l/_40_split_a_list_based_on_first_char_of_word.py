'''
#40. req:split a list based on the first character of the word?

1. CRUD       -->  retrieve
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =     | for/if/else

#0.mthematics:

1. take a list
2. import groupby and itemgetter from itertools
3.use for loop to iterate the words and letters of list
4. to get ordered list use sort function and group all the words,to get the word
based on first character use key as  itemgetter with starting index zero
5. print the letters
6. check whether words in words are not
7. if it is there print the words

#1. by using builtin functions:

#2. algorithm:

somelist = ['About', 'Absolutely', 'After', 'Aint', 'Alabama', 'AlabamaBill', 'All', 'Also', 'Amos', 'And', 'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill', 'Billgone']
from itertools import groupby
from operator import itemgetter
for letter, words in groupby(sorted(somelist), key=itemgetter(0)):
    print (letter)
    for word in words:
            print (word)

#3. by using functions:


def splitLst(x):
    dictionary = dict()
    for word in x:
       f = word[0]
       if f in dictionary.keys():
            dictionary[f].append(word)
       else:
            dictionary[f] = [word]
    return dictionary

print(splitLst(['About', 'Absolutely', 'After', 'Aint', 'Alabama', 'AlabamaBill', 'All', 'Also', 'Amos', 'And', 'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill', 'Billgone']))
'''
