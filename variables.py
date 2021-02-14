'''
practice - Assigning values to variables
'''
a = b = c = 10
print(a)
print(b)
print(c)

d,e,f = 10,20,30
print(d)
print(e)
print(f)

d,e,f = (10,20,30)
print(d)
print(e)
print(f)

d,e,f = [10,20,30]
print(d)
print(e)
print(f)

d,e,f = {10,20,30}
print(d)
print(e)
print(f)

a = (10,20,30)
d,e,f,g = a
print(d)
print(e)
print(f)
print(g)
#ValueError: need more than 3 values to unpack

