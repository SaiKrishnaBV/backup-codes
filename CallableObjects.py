class printing:
	def __init__(self, name):
		self.name = name
	
		
	def __call__(self):
		print("Entered name is:",self.name)
		
p = printing("sai")
p()
q = printing("krishna")
q()


'''
Defining a __call__ method in a class makes the objects of the class callable

All the inbuilt classes like type, len, list, tuple have __call__ implemented in the respective classes hence they are callable
'''
