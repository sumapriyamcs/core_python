'''
# P49. REQ : count and display the vowels of a given text
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
str_1 = 'asgtr1645jhgoi'
            ^^
            ||
         1           23
         vowel = 4

1. Initialize the string,take the string from the user
2. take the vowels from the user
3. take Count variable to store the vowels count
4.use for loop to iterate characters present in the string
5.use if condition to check whether that  string compared character present in vowels also are not
6.if the characeter present in vowels also,increment count value
7.finally,print count value of vowels


"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# Python Program to Count Vowels in a String

str1 = input("Please Enter Your Own String : ")

vowels = 0
str1.lower()

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1

print("Total Number of Vowels in this String = ", vowels)


# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = 'asgtr1645jhgoi'
print("String :", str_1)
vow = 'aeiou'
count = 0
for i in str_1:
    if i in vow:
        count += 1

print('Vowel count in String : ', count)


a_string = "Abcde"
lowercase = a_string.lower()
#Convert to lowercase

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
#Count vowels

    vowel_counts[vowel] = count
#Add to dictionary


print(vowel_counts)

#by using functions:
def vowel(string):
    vowels = 0
    for i in string:
          if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels=vowels+1
    print("Number of vowels are:")
    print(vowels)
string=input("Enter string:")
vowel(string)

'''
