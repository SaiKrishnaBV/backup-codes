'''
practice - list

* Mutable
'''

'''
----------------------- Mutable strings --------------------------------------------------------

word = "saikrishna"
word = list(word)
print(word)
word[0] = "S"
word[3] = "K"
print(word)
word = ''.join(word)
print(word)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Indexing ---------------------------------------------------------------
Indexing and slicing are similar to that used with strings.
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Operations on list -----------------------------------------------------

num = [1,3,5,7,9]
print("Sum of elements of list is: {}".format(sum(num)))
#Sum of elements of a list

print(3 in num)
#Check if an element is present in the list

new_num = num.append(11)
print(new_num)
print(num)
#append adds an element to the end of the list.
#append does not return the updated list, it directly updates the list

print(len(num))
#Returns the length of the list

num.insert(1,2)
print(num)
#to insert an element to the list at the desired index
#first argument is index
#second argument is the item


print(num.index(2))
#Returns the index corresponding to the first encounter of the argument in the list
#If the argument is not present in the list it returns ValueError: <ele> is not in list

ele = num.pop()
print(ele)
print(num)
#Removes the last element of the list, and returns it

ele = num.remove(5)
print(ele)
print(num)
#to remove a particular entry from the list
#It does not return anything, and directly operates on the list

del(num[1])
print(num)
#to remove element at a particular index, even remove can be used with index
num.remove(num[0])
print(num)

num.clear()
print(num)
#Empties the list, available only in python 3.x

del num
#print(num)
#Deletes the list completely
#The print statement prints: NameError: name 'num' is not defined

a = [1,2,3]
b = [4,5,6]
print(a+b)
a.append(b)
print(a)
a = [1,2,3]
b = [4,5,6]
a.insert(len(a),b)
print(a)
#You cannot use -1 to make insert work like append, as -1 for old "a" and new "a" are different

cars = ["benz","audi","toyota","hyundai","kia"]
cars.sort()
#Sort alphabetically
print(cars)

cars.sort(key = len)
#Sort based on the length
print(cars)

cars.sort(key = len, reverse = True)
#Sort based on the length in decreasing order
print(cars)
------------------------------------------------------------------------------------------------
'''


'''
----------------------- Shallow copy -----------------------------------------------------------

a = ['a','e','i','o','u']
b = a
print(a)
print(b)
a[4] = 'w'
print(a)
print(b)
b[1] = 'b'
print(a)
print(b)
#Using assignment operator with lists results in shallow copy, 
#i.e. changes made in one copy will be reflected in the other as well
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Deep copy --------------------------------------------------------------

a = [1,2,3,4,5]
b = a.copy()
print(a)
print(b)
a[4] = 4.5
print(a)
print(b)
b[4] = 5.75
print(a)
print(b)
#Since it is deep copy, the changes performed on one list is not reflected in the other
------------------------------------------------------------------------------------------------
'''

'''

try this

>>> a = [1,2]
>>> id(a)
139733790971592
>>> a+=[3]
>>> id(a)
139733790971592
>>> a = a + [3]
>>> id(a)
139733790972104

with functions passing lists to function
'''








'''
----------------------- Replace method ---------------------------------------------------------
------------------------------------------------------------------------------------------------
'''
