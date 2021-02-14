prod = []
count = int(input())
for i in range(count):
	name = input("Enter name of the product: ")
	cost = int(input("Enter price: "))
	desc = input("Enter description: ")
	tag = "ID" + str(i)
	prod.append({"name":name, "price":cost, "description":desc})
	
#print(prod)
print("Name","Price","Description", sep = '\t')
for i in prod:
	print(i["name"],i["price"],i["description"],sep = "\t")
