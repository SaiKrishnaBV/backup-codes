'''
Practice - tuples
* Immutable
'''

num = (2,3,5,7,11)

'''
----------------------- Immutable --------------------------------------------------------------

num[0] = 1 	#TypeError: 'tuple' object does not support item assignment
print(num)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Accessing elements -----------------------------------------------------

print(num[0])
print(num[-1])
#Indexing and slicing is similar to that of lists and string
------------------------------------------------------------------------------------------------
'''

'''
----------------------- tuple Operations -------------------------------------------------------

print("Sum of elements of list is: {}".format(sum(num)))
#Sum of elements of a list

print(3 in num)
#Check if an element is present in the list

#new_num = num.append(11)  #AttributeError: 'tuple' object has no attribute 'append'

print(len(num))
#Returns the length of the tuple


print(num.index(2))
#Returns the index corresponding to the first encounter of the argument in the tuple
#If the argument is not present in the tuple it returns ValueError: <ele> is not in tuple

del num
#print(num)
#Deletes the tuple completely
#The print statement prints: NameError: name 'num' is not defined

a = (1,2,3)
b = (4,5,6)
print(a+b)

num = (1,2,2,5,43,12,2,52)
print(num.count(2))
#Prints the number of times the argument is repeated
------------------------------------------------------------------------------------------------
'''


