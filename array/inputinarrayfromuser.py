from array import *
arr=array('i',[])
""" for taking input from user in the array


n=int(input("enter the length of array")) 

for i in range(n):
    x=int(input("enter the next value "))
    arr.append(x) """
print(arr)
key=int(input("enter the number to be found"))
""" method 1 for searching the element in  the array
for e in range(n):

    if(arr[e]==key):
        print( "the index number is ", e )
        break
else:
    print("the number is not in the array") """
print(arr.index(key))
