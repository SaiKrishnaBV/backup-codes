'''
positional parameters

* Optional parameters 
* If not passed it takes the default value
* Parameter names can be used in the calling function
* Position does not matter
* Non keyword argument cannot be given after keyword argument
'''


def add(n1 = 2, n2 = 5):
	print("n1: " + str(n1))
	print("n2: " + str(n2))
	return n1+n2
	
print(add(3,6))
print("-"*20)
print(add())
print("-"*20)
print(add(4))
print("-"*20)
print(add(n1=5,n2=12))
print("-"*20)
print(add(n2=6))
print("-"*20)
# print(add(n2=8,6))    SyntaxError: non-keyword arg after keyword arg
# print(add(6,n1=8))	TypeError: add() got multiple values for keyword argument 'n1'
print(add(6,n2=8))
print("-"*20)

'''
def m():
	print("hello")
	def m2():
		return 10
	return m2
	
print(m()())
'''

#Passing variable number of arguments to a function
def maximum(*args):
	return max(args)
	
print(maximum(-12,12,14,43,11,0))
print(maximum(140,43,11,0))
print(maximum(11,0))

