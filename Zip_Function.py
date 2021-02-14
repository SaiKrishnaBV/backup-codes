'''
practice - zip()

* returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

* If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
'''
import sys

a = [1,2,3,4,5]
b = [1,4,9,16,25]
c = [1,8,27,64,125,216]
z = zip(a,b,c)
print(z)
print(sys.getsizeof(z))

d = [4,2,8,1,3]
greater = []
for x,y in zip(a,d):
	greater.append((y,x) [x>y])
	
print(greater)


a = [1,2,3,4,5,6,7,8,9,10]
b = [x**2 for x in a]
zipped = zip(a,b)
print(type(zipped))
print(sys.getsizeof(zipped))
print(zipped)
vals = list(zipped)
print(vals)
