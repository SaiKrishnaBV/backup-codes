'''
Ellipsis is used to automatically select indices in case of high dimensional arrays

* ... is the ellipsis object

'''
import numpy as np

d = np.array([[[i+2*j+8*k for i in range(3)] for j in range(3)] for k in range(3)])
print(d)
print(d[...])
print("-"*30)
print(d[1,...])
print("-"*30)
print(d[...,2])
