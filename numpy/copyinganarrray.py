from numpy import *

#direct  changes in each element

arr=array([1,2,3,4,5])
arr=arr+5
print(arr) 
#adding two array this is called vectorized addition
 
arr2=array([ 6 , 7 , 8 , 9 ,10])
arr3=arr+arr2
print(arr3) 

#basic operation done in the array
print(sum(arr))
print(concatenate([arr2,arr3]))

