'''
Generators:

* Produces or yields a sequence of values using yield method

* When next() method is called, it will execute until it reaches the yield statement
'''

import sys

def fib(n):
	a,b,counter = 0,1,0
	
	while True:
		if(counter > n):
			return
			
		yield a
		a, b = b, a+b
		counter += 1
		
f = fib(6)
# f is an iterator object
print("Size of generator:",sys.getsizeof(f))
for n in f:
	print(n)
fib_num = [0,1,1,2,3,5,8]
print("Size of list:",sys.getsizeof(fib_num))
while True:
	try:
		print(next(f), end = ' ')
	except StopIteration:
		sys.exit()
		
'''
def gennos():
	l = []
	for n in range(1,51):
		l.append(n)
		if(n%10 == 0):
			yield l
			l = []
			
gen = gennos()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''
		
'''
Advantages of Generator over a list

1) Generator takes much less memory
2) yields one item at a time, hence it is more memory efficient. Where as with the entire list is stored in memory
'''
