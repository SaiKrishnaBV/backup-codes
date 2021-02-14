'''
NameSpace

* namespace is a collection of names.

* Different namespaces can co-exist at a given time but are completely isolated.

* Types
	- Built-in NameSpace
	- Global Namespace
	- Local Namespace
	
* 
'''
def f1():
	p = 23
	q = 4.15
	print("Inside function")
	print(dir())

a = "hello"
b = 2
c = 3.14
d = [1,2,3,5]
e = (1,2,3,5,6,7)
f = {"Ind":1,"SA":2}
print(dir())
f1()

#dir() prints all the variables part of the current namespace
