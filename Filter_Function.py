'''
Filter method

* constructs an iterator from elements of an iterable for which a function returns true

* filter(function, iterable) is the syntax

'''

a = [1,2,3,4,5,6,7,8]
print(filter(lambda x: x%2 == 0,a))      #lazy evaluation
print(list(filter(lambda x: x%2 == 0,a)))

def sqr(x): return x**2

print(list(filter(lambda x: x%3 == 0,list(map(sqr,a)))))    #Returns the squares of first 8 natural numbers that are divisible by 3


nums = [-1,2,-3,5,7,8,9,-10]
print(list(filter(lambda x: x<0,nums)) + list(filter(lambda x: x>0,nums)))

array_nums1 = [1,2,4]
array_nums2 = [2,4,6]
print(list(set(list(filter(lambda x: x in array_nums1, array_nums2)) + list(filter(lambda x: x in array_nums2, array_nums1)))))

print(list(filter(lambda x: x in array_nums1, array_nums2)))
