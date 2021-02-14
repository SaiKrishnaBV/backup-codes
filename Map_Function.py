'''
map function

* To apply an operation to each element of the collection

* map(function, Collection) applies function to every item in Collection

* lazy evaluation

	is an evaluation strategy which delays the evaluation of an expression until its value is needed
'''
a = [1,2,3,4,5,6,7,8]
def sqr(x): return x**2

print(map(sqr,a))                #LAZY evaluation
print(list(map(sqr,a)))

print(list(map(lambda x: x*x, a)))

b = [1,2,3,4,5,6,7,8]
print(list(map(lambda x,y: x+y, a, b)))  #map with multiple iterables
