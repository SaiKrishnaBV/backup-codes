'''
practice - Basic math operators
'''

a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
#If both operators are int, then int part of the quotient is printed

print(float(a/b))
#Wont work, as we are converting to float after performing the division

a = 10.0
b = 20.0
print(a/b)
#Both operands are float, hence the quotient will also be float

print(a//b)
#floor(quotient) is returned

a = 2
b = 4
print(a**b)
#Exponentiation a^b

a = 12
b = 5
print(a%b)
#Remainder

print(bool(0))   		#False
print(bool(1))   		#True
print(bool(0.0000000000001))    #True
print(bool(""))			#False
print(bool("false"))		#True

'''
Precedence of boolean operators
not > and > or
'''
print("-"*20)
a = 4
b = 4
print(a is b)

a = "Hello"
b = 'Hello'
print(a is b)

a = [1,2,3]
b = [1,2,3]
print(a is b)

a = (1,2,3)
b = (1,2,3)
print(a is b)

a = b = [1,2,3]
print(a is b)
# is checks if both the arguments are pointing to the same object
# == checks if the elements of the object are same or not

