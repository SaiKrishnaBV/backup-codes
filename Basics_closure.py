'''
To call nested functions outside its scope
'''
def outer():
	x = 3
	print("inside outer()")
	def inner():
		y = 3
		return x + y
	return inner
	
a = outer()
# inner()       -> will give an error as the call is made outside the scope of inner
print(a.__name__)

print(a())   
#inner() is called outside its scope , this is called closure

'''
Closure:
	Function object that remembers values in the enclosing scope even if they are not present in memory
'''
