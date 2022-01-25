'''

# P56. REQ :  find the 2nd most repeated word in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |  +=    =    |   for, if/else
"""

# 0. Mathematics
"""
1. take a string
2. split that string
3. stored the splited string in one variable
4.to find the repeated word take one variable as zero
5.use for loop to iterate words present in the string
6. use if condition to compare whether the count of i value greater than taken variable are not
7.if it is greater  store in taken variable
8. that greater i  is max character
9.print the result


"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

string = input("Enter a string :-")
lst = string.split()
max = 0
for i in lst:
    if lst.count(i) > max :
        max = lst.count(i)
        maxvalue = i

print(maxvalue)

#algorithm:

# Python3 code to demonstrate working of
# Most frequent word in Strings List
# Using list comprehension + mode()
from statistics import mode

# initializing Matrix
test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is best"]

# printing original list
print("The original list is : " + str(test_list))

# getting all words
temp = [wrd for sub in test_list for wrd in sub.split()]

# getting frequency
res = mode(temp)

# printing result
print("Word with maximum frequency : " + str(res))

# Python3 code to demonstrate working of
# Most frequent word in Strings List

from collections import Counter

# function which returns
# most frequent word
def mostFrequentWord(words):
    # Taking empty list
    lis = []
    for i in words:

        # Getting all words
        for j in i.split():
            lis.append(j)

    # Calculating frequency of all words
    freq = Counter(lis)

    # find max count and print that key
    max = 0
    for i in freq:
        if (freq[i] > max):
            max = freq[i]
            word = i
            return word


# Driver code
# initializing strings list
words = ["gfg is best for geeks", "geeks love gfg", "gfg is best"]

# printing original list
print("The original list is : " + str(words))

# passing this words to mostFrequencyWord function
# printing result
print("Word with maximum frequency : " + mostFrequentWord(words))



from collections import Counter

# Example phrase
phrase = "John is the son of John second. Second son of John second is William second."
split_phrase = phrase.split()

# create counter object
Counter = Counter(split_phrase)

most_occured_words = Counter.most_common(4)

print(most_occured_words)

#3. by using functions:

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # print(counts_x)
    return counts_x[-2]
print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints()."))

'''
