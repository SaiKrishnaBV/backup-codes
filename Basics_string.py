'''
Practice - Strings

* Immutable
'''

'''
----------------------- Replace method ---------------------------------------------------------

word = "saikrishna"
print(word.replace("sa","Sa"))
print(word.replace("s","S"))
print(word.replace("s","S",1))

# The third argument passed is the number of times we want the replacing to happen
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Sub-String method ------------------------------------------------------

word = "saikrishna"
sub = word[1]
print(sub)

#Starting index - inclusive
#Ending index - exclusive
sub = word[1:6]
print(sub)

#If nothing is mentioned for starting index by default it is the beginning of the word
sub = word[:6]
print(sub)

#If nothing is mentioned for ending index by default it is the end of the word
sub = word[3:]
print(sub)

#If nothing is mentioned for both the indices, then it is the full word
sub = word[:]
print(sub)

#The third argument passed is the value by which it has to skip, by default it is 1
sub = word[::2]
print(sub)

#If the third argument is -1, then it will reverse the string
#If any other negative number is used, then characters in the reversed string are skipped with that value
sub = word[::-1]
sub1 = word[::-2]
print(sub)
print(sub1)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- positive and negative indexing -----------------------------------------

word = "saikrishna"
print(word[0])   #Starts from leftmost letter
print(word[-1])  #Starts from rightmost letter

sub = word[-1:-6:2]
print(sub)
#Prints empty string bcoz, -1+2 = 1 index 1 is not part of the slicing
#For right indexing, start index should be smaller than stop index

sub = word[-1:-6:-2]
print(sub)
#Starts at index -1, (-1-2) = -3, (-3-2) = -5, (-5-2) = -7 (Not part of the slicing).
#Prints word[-1]word[-3]word[-5]
------------------------------------------------------------------------------------------------
'''

'''
------------------- Strings are immutable ------------------------------------------------------

word = "saikrishna"
word[0] = "S"
print(word)

#output: TypeError: 'str' object does not support item assignment
------------------------------------------------------------------------------------------------
'''

'''
----------------------- String operations ------------------------------------------------------

sentence = "The weather is bright today"
words = sentence.split(" ")
print(words)
# Splits the string whenever space is encountered

word1 = "hello"
word2 = "world"
print(word1 + " " + word2)
#String concatenation

print("%s %s"%(word1,word2))
#% is used as format specifier, that indicates the type of the data to be added there.

print("{} {}".format(word1,word2)) 
#Alternative for format specifier, useful when the type of the variable is unknown

print("{1} {0}".format(word2,word1))

word1 = "hello123"
print(word1.upper())
#Converts all letters of the string to upper case

print(word1.lower())
#converts all letters of the string to the lower case

print(word1.capitalize())
#Converts only the first letter to upper case

print(len(word1))
#Prints the length of the string

print(word1.strip("123"))
#removes the specified characters from the string from the ends of the string
#if no argument is passed it will trim the white spaces at the end of the string
#if argument passed does not occur at the end of the string it does not modify the string

print("hello" in word1)
#To check if the string contains a particular word

word1 = "abcabcabc"
print(word1.count("abc"))
#Count the number of times the argument is repeated in the string

word1 = "abcdefghijk"
print(word1.find("z"))
#Returns the index of the argument in the string, if not found returns -1

num = "323a"
num1 = "a123"
print(num.isdigit())
print(num1.isdigit())
#Checks if all characters in the string are numbers or not

------------------------------------------------------------------------------------------------
'''

'''
----------------------- Format specification for print() ---------------------------------------

num = "12"
num2 = "34"
num3 = "56"
print(num,num2,num3, sep ="*",end =" end of print statement\n")
#Available only in python3.x
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Equality check ---------------------------------------------------------
a = "sai"
b = a
print(a)
print(b)
print(a==b) #Checking if two strings are same

a = "krishna"
print(a)
print(b)
print(a is b) #Checking if two strings are same
------------------------------------------------------------------------------------------------
'''

'''
----------------------- '..' ".." are same -----------------------------------------------------

a = "sai"
b = 'krishna'
print(a + " " + b)
print(a + ' ' + b)
------------------------------------------------------------------------------------------------
'''


'''
----------------------- quotes in a string -----------------------------------------------------

print('His name was "john"')
print("His name was \"john\"")
#to print double quotes inside a string

print("His name was 'john'")
print('His name was \'john\'')
#to print single quote inside a string
------------------------------------------------------------------------------------------------
'''









'''
----------------------- Replace method ---------------------------------------------------------
------------------------------------------------------------------------------------------------
'''

