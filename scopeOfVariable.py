'''
scope of variable

* 1)local scope
	Contains names defined inside the current function
	
  2)global
  	Contains names defined at the top-level of the module/script
  	
  3)enclosed
  	Contains names defined inside any and all enclosed functions (nested functions)
  	
  4)built-in
  	Contains names built_in to the python programming language   Ex: print(), len()
'''

val = 25
global num
num =50

def f1(val):
	print("Inside f1: " + str(val))
	val = 10
	print("Inside f1 modified value: " + str(val))
	
def f2():
	print("Inside f2: " + str(val))
	#Since there is no value for variable val locally defined 
	#it will next search globally and use that variable and it wont throw an error
	'''
	val = 45
	print("Inside f2 modified value: " + str(val))
		UnboundLocalError: local variable 'val' referenced before assignment
	'''
	#Only the value of val can be accessed inside f2, but it cannot be changed even locally
	
def f3():
	global num
	print("Inside f3: " + str(num))
	num = 32
	print("Inside f3 modified value: " + str(num))
	'''
	Since global variable is used, any changes made to it will affect the value globally and not locally
	'''
	
def f4():
	global val
	print("Inside f4: " + str(val))
	val = 110
	print("Inside f4 modified value: " + str(val))
	
	
print("Global value: " + str(val))
f1(12)
print("Global value after f1: " + str(val))
f2()
print("Global value after f2: " + str(val))
print("Global value of num: " + str(num))
f3()
print("Global value of num after f3: " + str(num))
print("-"*20)
print("Global value: " + str(val))
f4()
print("Global value after f4: " + str(val))
