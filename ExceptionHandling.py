'''
practice - Exception Handling

1) Syntax error
2) Logic error
3) Exceptions

Assertion Error     - When assert statement fails
Attribute Error     - When attribute assignment or reference fails
EOF Error           - When input() function hits end-of-file condition
FloatingPoint Error - When floating point operation fails
Import Error        - imported module is not found
Indentation Error   - When there is incorrect indentation
Index Error	    - index of a sequence is out of range
Key Error	    - Key is not found in dictionary
Memory Error        - When operation runs out of memory
Name Error          - When variable is not found in local or global scope
OS Error            - When system operation causes system related error
Overflow Error      - Result of expression is too large to be represented
Runtime Error       - When the error does not fall under any other category
Syntax Error        - Raised by parser when syntax error is encountered
Type Error          - When a function/operation is applied to an object of incorrect type
UnboundLocal Error  - When a reference is made to a local variable, but no value has been bound to that variable
Value Error         - When a function gets argument of correct type but improper value
ZeroDivision Error  - When tried to divide a number by 0

'''

'''
----------------------- ZeroDivision Error -----------------------------------------------------

try:
	print(5/0)
except ZeroDivisionError:
	print("Division by zero not possible")
finally:
	print("You are inside finally block")
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Assertion Error --------------------------------------------------------

try: 
	def KelvinToFahrenheit(temp):
		assert(temp>=0), "Colder than absolute zero"    
		#If not used inside try block, Assertion Error: Colder than absolute zero is printed
		return (temp-273)*1.8 + 32
	
	print(KelvinToFahrenheit(273))
	print(KelvinToFahrenheit(-2))
except AssertionError:
	print("Assertion Error")


------------------------------------------------------------------------------------------------
'''

'''
----------------------- Any possible Error -----------------------------------------------------

try:
	print("Hello World")
except:
	print("Some error occured")		     #except: to catch any possible exception
else:
	print("inside else block")                   #executed when there is no exception
finally:
	print("inside finally block")		     #always executed
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Multiple Error ---------------------------------------------------------

try:
	a = [1,2,3]
	b = a[4]/0
except (IndexError, ZeroDivisionError):
	print("One of IndexError or ZeroDivisionError has occured")
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Multiple Except --------------------------------------------------------

try:
	a = [1,2,3]
	b = a[4]/0
except ZeroDivisionError:
	print("division by zero not possible")
except IndexError:
	print("List index out of range")
------------------------------------------------------------------------------------------------
'''
