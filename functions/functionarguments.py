from  numpy import *
"""
here  value does not cahnge and the address is also get  changed the moment its updation beacuse int is immutable
 def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)

a=10
print(id(a))
update(a)
print("a",a) """

""" 
the value get  cchanged but not the address because list is mutable objects
def update(lst):
    print(id(lst))
    lst[1]=10
    print(id(lst))
    print("x",lst)

lst=[25,26,30]
print(id(lst))
update(lst)
print("lst",lst) """

