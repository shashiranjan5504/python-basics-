from numpy import *
arr1=array([2,6,8,1])

#shallow copy
arr2=arr1.view()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


#deep copy
arr2=arr1.copy()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))