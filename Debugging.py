'''
debugging

* Functionalities of a debugger
	- Identify the flow of the program
	
* pdb module can be used to debug python code

* use s to step through the code line by line
	<Procedure to debug from terminal>
		
		python3
		import Debugging
		import pdb
		
		pdb.run('calculation(20,5)')
		NameError: calculation is not defined
		
		copy paste the code for all functions
		
		pdb.run('calculation(20,5)')
		s -> step through the code line by line
		
	<Procedure to debug the code within the program>

* pdb.py can be invoked asa script to debug other scripts by executing: python3 -m pdb myscript.py

  1) Navigate the execution stack - with where, list, up, down commands
  2) Examine variables on the stack - with args a, print p, pp commands
  3) Step through the program with step, next, until, return commands
'''
import pdb

def addition(a,b):
	c = a + b
	return c
	
def division(a,b):
	c = a/b
	return c
	
def calculation(a=0,b=0):
	#pdb.set_trace()      -> Use this to debug the program from inside, run python3 Debugging.py 
	
			      #if set_trace() is not used use python3 -m pdb Debugging.py  to debug the program
	add = addition(a,b)
	div = division(a,b)
	'''
	div = division(a,c)
	
	
	Terminal - python3
	>>> import Debugging.py
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/krishna/SK/python/Debugging.py", line 52, in <module>
	    calculation(20,5)
	  File "/home/krishna/SK/python/Debugging.py", line 48, in calculation
	    div = division(a,c)
	NameError: name 'c' is not defined
	>>> import pdb
	>>> pdb.pm()
	> /home/krishna/SK/python/Debugging.py(48)calculation()
	-> div = division(a,c)
	(Pdb) 
	
	
	* It will directly show the line where there is an error
	
	'''

	result = add * div
	return result
	
calculation(20,5)
