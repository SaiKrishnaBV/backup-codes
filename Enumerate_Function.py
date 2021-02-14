'''
Enumerate function

* Adds counter to an iterable and returns the enumerated object

* enumerate( iterable, start = <startIndex> )
	default startIndex  = 0
'''
import sys

a = [1,4,9,16,25,36,49,64,81,100]
indexed_sqr = enumerate(a, start = 1)
print(indexed_sqr)
print(type(indexed_sqr))
print(sys.getsizeof(indexed_sqr))
vals = list(indexed_sqr)
print(vals)

