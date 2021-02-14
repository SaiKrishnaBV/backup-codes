'''
practice - FILE IO

* 'w' ->  Write mode
* 'r' ->  Read mode
* 'a' ->  Append mode
* 'r+' -> Read and Write mode

* .write() -> 	 to write to the file
* .read() -> 	 Read from a file
* .readline() -> Read line by line

* Explicily closing the file is not needed when using "with" "as"
'''

#Writing to a file
data = [1,2,3,4,5,6,7,8,9]
my_file = open("fileData.txt","w")

for item in data:
	my_file.write(str(item) + "\n")    #write always takes string argument
	
my_file.close()

#Reading from a file
my_file = open("fileData.txt","r")
print("Reading file line by line")
print(my_file.readline())

print("Reading entire file from here")
print(my_file.read())   # my_file.readlines() can also be used to read the entire file. It returns a list, with each line in the file as an
			# element of the list

my_file.close()

print("-"*20)


#Write and Read using "with" "as" keywords
with open("withas.txt","w") as my_file:
	my_file.write("This is an example of with-as write/read operation")
	print("Written")
	
with open("withas.txt","r") as read_file:
	print(str(read_file.read()))


