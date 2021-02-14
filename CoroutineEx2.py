'''
* event loop is the core of every asyncio application. It runs in a thread (typically the main thread) and executes all callbacks and
  tasks in its thread
  
'''
import asyncio

async def main():
	#print("Hello",end=" ")
	print("Hello")
	await userPrint()     #execution of current coroutine is stopped until the execution of the code in await is not finished
	print("World")

async def userPrint():
	print("Inside userPrint()")	


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
