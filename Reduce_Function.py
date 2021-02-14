'''
Reduce function

* Transforms the given list into a single value by applying a given function continuously to all elements of the list (takes two elements at a time)

* reduce(function, list)
'''

from functools import reduce

a = [1,2,3,4,5,6,7,8]
prod = reduce((lambda x,y: x*y),a)
print(prod)
print(reduce(lambda x,y: x+y, a, 10))  #initial value taken is 10 and then the elements of the list are added
				       # it is equivalent to adding 10 to the sum of elements of the list
