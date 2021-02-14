'''
practice - lambda functions

* A lambda function is a small anonymous function.
* Can have only one expression
'''

'''
----------------------- Simple functions -----------------------------------------------------

cube = lambda x:x*x*x
print(cube(5))

maximum = lambda a,b: a if a>b else b
print(maximum(5,6))
----------------------------------------------------------------------------------------------
'''

'''
----------------------- Tuples for selection based on condtion -------------------------------
a = 10
b = 25
print( (b, a) [a > b] )
print({True:a, False:b} [a>b])
print((lambda: b, lambda: a)[a > b]())
# (if_test_false,if_test_true)[test]
----------------------------------------------------------------------------------------------
'''
from functools import reduce
a = [0,1]
b = [1,1]
a.extend(list(map(lambda x,y: x + y,a,b)))
print(list(map(lambda x,y: x + reduce(lambda x,y: x+y, a),a)))
print(a)



