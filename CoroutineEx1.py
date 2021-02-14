'''
function - subroutine, procedure, subprocess

* Coroutines are generalization of subroutines. They are used for cooperative multitasking

* Coroutines have multiple entry points unlike subroutine

* Coroutine can suspend its execution and transfer control to other Coroutine and can resume again execution from point it left off

* Coroutine vs threads
	Incase of threads OS switches btw threads according to the scheduler
	
	Incase of Coroutine, programmer and programming language decide when to switch
	
* to define a coroutine use the following syntax:
	async def <func_name>():
'''
async def hello():
	print("Hello world")
	
hello()
#It returns an error
'''
	CoroutineEx1.py:21: RuntimeWarning: coroutine 'hello' was never awaited
	
	* When a coroutine is called, the body of the coroutine is not executed but an object of coroutine is created
	
	* to pause a coroutine use "await" keyword 
	
	* task is used to schedule multiple coroutines
'''
