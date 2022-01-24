
# P27. REQ :  remove existing indentation from all of the lines in a given text
"""
1. CRUD       -->  delete
2. STATE      -->  string
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""
1. import textwrap
2. take a string
3.print taken string
4. use dedent with string to remove indentation
5. use textwrap with 4 step to get the result
6. use 4&5 steps in print statements  to get final proper result to user

"""

# 1.Builtin functions
import textwrap
s = '''
       example
       string
    '''
print(s)
print(textwrap.dedent(s))

#2. algorithm:

print("--------1 Builtin Functions      ----------")

import textwrap
sample_text = ''' 
America is a beautiful country, actually its official name is United States of America. It's capital is Washington DC.
 Other famous cities in US are New York, Detroit, Chicago, New Jersey, Philadelphia, Florida, San Francisco, Houston, 
 Las Vegas, Seattle, Boston, Miami, Phoenix. The population of the country is about 333 Million with people originating
  from all over the world. Some famous landmarks and sites in worth visiting are statue of liberty in New York, casinos 
  at Las Vegas, Golden Gate bridge at San Francisco, Hollywood, Harvard University, The Capitol and the Gran Canyon. 
  One may spend a lifetime exploring places and sites in America but that won't be enough to cover all of them. Indeed,
   this country is truly blessed with variety of climates, diverse geography, rich flora and fauna and of course 
   wonderful people.
  '''
print("String :", sample_text)
text_without_Indentation = textwrap.dedent(sample_text)
print()
print("Exp. o/p :", text_without_Indentation)

#3.by using functions:

print("--------3 Functions      ----------")
def remove(sample_text):

    import textwrap
    text_without_Indentation = textwrap.dedent(sample_text)
    print()
    print("Exp. o/p :", text_without_Indentation)

sample_text = ''' 
America is a beautiful country, actually its official name is United States of America. It's capital is Washington DC.
 Other famous cities in US are New York, Detroit, Chicago, New Jersey, Philadelphia, Florida, San Francisco, Houston, 
 Las Vegas, Seattle, Boston, Miami, Phoenix. The population of the country is about 333 Million with people originating
  from all over the world. Some famous landmarks and sites in worth visiting are statue of liberty in New York, casinos 
  at Las Vegas, Golden Gate bridge at San Francisco, Hollywood, Harvard University, The Capitol and the Gran Canyon. 
  One may spend a lifetime exploring places and sites in America but that won't be enough to cover all of them. Indeed,
   this country is truly blessed with variety of climates, diverse geography, rich flora and fauna and of course 
   wonderful people.
  '''
print("String :", sample_text)
remove(sample_text)