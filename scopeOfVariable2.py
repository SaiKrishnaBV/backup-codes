'''
Understanding the concept of nonlocal variables(enclosed variables) inside nested functions
'''
z = 5
def in_func():
	z = 10
	print("In_func() --> local: z =",z)
	def inner_func():
		nonlocal z         #to access enclosed variable instead of global variable
		z+=1
		print("Inner_func() --> z =",z)
		def innermost_func():
			#global z
			#print("Innermost_func() --> global: z =",z)
			nonlocal z
			print("Innermost_func() --> nonlocal: z =",z)
		innermost_func()
		print("After CALL: Inner_func() --> nonlocal: z=",z)	
	inner_func()
	print("After CALL: In_func() --> local: z=",z)
		
			
in_func()
print("After CALL: main() --> global: z=",z)

			

