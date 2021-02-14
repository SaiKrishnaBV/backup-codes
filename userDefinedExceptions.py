'''
User defined Exceptions
'''

class Error(Exception):
	''' Base class for other exceptions'''
	pass
	
class ValueTooSmallError(Error):
	'''Raised when input value is too small'''
	pass
	
class ValueTooLargeError(Error):
	'''Raised when input value is too large'''
	pass
	
number = 10
while True:
	try:
		guess = int(input("Enter a number: "))
		if(guess < number):
			raise ValueTooSmallError
		elif(guess > number):
			raise ValueTooLargeError
		else:
			print("your guess is correct")
		break
	except ValueTooSmallError:
		print("Entered value is smaller than actual number, try again.!!")
	except ValueTooLargeError:
		print("Entered value is larger than actual number, try again.!!")
