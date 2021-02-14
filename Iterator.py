'''
Iterators

* Allows a programmer to travere through all elements of a collection

* An iterator object implements two functions iter() and next()
'''
import sys

a = [1,2,3,4,5,6]
it = iter(a)       #builds the iterator object
while True:
	try:
		print(next(it))
		
	except StopIteration:
		print("You have reached the end of the iterable")
		sys.exit()

