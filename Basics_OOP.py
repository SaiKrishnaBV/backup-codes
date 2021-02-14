'''
magic methods:  begin with __<..>__
Ex: __init__
    __name__
    
* To declare private variables the variable name should begin with __<varname>
    
'''
class Car:
	num_Wheels = 4 
	def __init__(self, model):
		self.model = model
		
	def drive(self):
		print("Car started..")
		
	def stop(self):
		print("Car stopped")
		
class Audi(Car):
	def __init__(self,model, price):
		super().__init__(model)
		self.price = price
		
	def light(self):
		print("Audi lights ON.")
		
		
	def drive(self):
		super().drive()
		print("You are driving an Audi car")
		
	def __str__(self):
		return str(self.price) + str(self.num_Wheels) + str(self.model)
		#similar to toString() in java
		
	def __eq__(self, other):
		return True if self.model == other.model else False
		# to compare the objects of the class using ==
		
		
c = Car("Sedan")
c.drive()
print("Model:",c.model)
c.stop()
c.num_Wheels = 3
print(c.num_Wheels)
print()
a = Audi("Q7", 100000)
a.drive()
print("Model:",a.model)
a.light()
a.stop()
print(a.num_Wheels)
print(a)

#b = a   #shallow copy
#b.price = 50000

b = Audi("Q7", 100000)
print(a == b)
print(a.price)
print(b.price)
