'''


# P55. REQ :  find the first repeated word in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |   for, if/else
"""

# 0. Mathematics
"""
1.First split given string separated by space.

2.Now convert list of words into dictionary using collections. Counter(iterator)
method. Dictionary contains words as key and it's frequency as value.

3.Now traverse list of words again and check which first word has frequency greater than 1.

4. the word is greater than one print that word.

                  (and)


1.Define a string.

2.Convert the string into lowercase to make the comparison insensitive.

3.Split the string into words.

4.Two loops will be used to find duplicate words. Outer loop will select a word
and Initialize variable count to 1.
Inner loop will compare the word selected by outer loop with rest of the words.

5.If a match found, then increment the count by 1 and set the duplicates of word
to '0' to avoid counting it again.

6.After the inner loop, if count of a word is greater than 1 which signifies
that the word has duplicates in the string.

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
str_1 = "ab ca bc ab ca ab"
print("String :", str_1)
str_2 = str_1.split(' ')
print("String :", str_2)
count = 0
for i in set(str_2):
    print("%s" % i, 'count', str_2.count(i))
    count += 1

# 2. Algorithm
print("--------2 Algorithm              ----------")


string = "big  bug bit a big  dog on his big black nose";

# Converts the string into lowercase
string = string.lower();

# Split the string into words using built-in function
words = string.split(" ");

print("Duplicate words in a given string : ");
for i in range(0, len(words)):
   count = 1;
   for j in range(i + 1, len(words)):
      if (words[i] == (words[j])):
         count = count + 1;
         # Set words[j] to 0 to avoid printing visited word
         words[j] = "0";

         # Displays the duplicate word if count is greater than 1
   if (count > 1 and words[i] != "0"):
      print(words[i]);

#3. by using functions:

# Function to Find the first repeated word in a string
from collections import Counter

def firstRepeat(input):
    # first split given string separated by space
    # into words
    words = input.split(' ')

    # now convert list of words into dictionary
    dict = Counter(words)

    # traverse list of words and check which first word
    # has frequency > 1
    for key in words:
        if dict[key] > 1:
            print(key)
            return


# Driver program
if __name__ == "__main__":
    input = 'Ravi had been saying that he had been there'
    firstRepeat(input)


# Python program for the above approach
from collections import Counter
# Python program to find the first
# repeated character in a string
def firstRepeatedWord(sentence):
    # spliting the string
    lis = list(sentence.split(" "))

    # Calculating frequency of every word
    frequency = Counter(lis)

    # Traversing the list of words
    for i in lis:

        # checking if frequency is greater than 1

        if (frequency[i] > 1):
            # return the word
            return i


# Driver code
sentence = "suma told to her mom now suma is very happy"
print(firstRepeatedWord(sentence))



def first_repeated_word(str1):
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'
print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc ab ca ab bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))

'''



