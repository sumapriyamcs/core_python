'''

# P62. REQ :   reverse a each word and reverse that word again in given string?

"""
1. CRUD       -->  update
2. STATE      -->  String
3. BEHAVIOR   -->   str    |  ::   =    |for
"""

# 0. Mathematics

1.Separate each word in given string using split() method of string data type in python.
2.Reverse the word separated list.
3.Print words of list, in string form after joining each word with space using ” “. join()
method .
4. again reverse the reversed words take another variable to reverse
5. join the words by using join function " ".join().
6. print the result

                        (and)
1.Take the string input from user.
2.Split the string using split() function.
3.Use the reverse() method to reverse all the words that have been split from the string.
4.Finally, join and print them using the join() function.
5. again reverse the reversed words take another variable to reverse
6. join the words by using join function " ".join().
7. print the result

                    (and)#for reverse each word
Step 1 : input a sentence. And store this in a variable s.
Step 2 : Then splitting the sentence into a list of words.
   w=s.split(“”)
Step 3 : Reversing each word and creating a new list of words nw.
Step 4 : Joining the new list of words and make a new sentence ns.

#1. builtin functions:

## initializing the string
string = "I am a python programmer"
print(string)
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
print(words)
words1=list(reversed(words))
print(words1)
## joining the words and printing
print(" ".join(words))
print(" ".join(words1))

#2. algorithm


s="hello world "
for line in s.split('\n'):
        print(' '.join(line.split()[::-1]))

#3.by using functions:

def rev(string):

    ## splitting the string on space
    words = string.split()
    ## reversing the words using reversed() function
    words = list(reversed(words))
    print(words)
    words1=list(reversed(words))
    print(words1)
    ## joining the words and printing
    print(" ".join(words))
    print(" ".join(words1))

## initializing the string
string = "I am a python programmer"
print(string)
rev(string)


def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))

'''


#  Reverse each word of a Sentence
# Function to Reverse words
def reverseword(s):
    w = s.split(" ")  # Splitting the Sentence into list of words.
    # reversing each word and creating a new list of words
    # apply List Comprehension Technique
    nw = [i[::-1] for i in w]
    # Join the new list of words to for a new Sentence
    ns = " ".join(nw)
    return ns

# Driver's Code
s = input("ENTER A SENTENCE PROPERLY ::")
print(reverseword(s))




s = input("ENTER A SENTENCE PROPERLY ::")
w = s.split(" ")  # Splitting the Sentence into list of words.
# reversing each word and creating a new list of words
# apply List Comprehension Technique
nw = [i[::-1] for i in w]
# Join the new list of words to for a new Sentence
ns = " ".join(nw)
print(ns)