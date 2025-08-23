""" 1.position
2.keyword
3.bydefault
4.variable length """
from numpy import *
def person(name,age=18):
    print(name )
    print(age-5)
person('shashi',25)

""" #example of positional argument
person(30,'ravi')#here  itgives error so actual argument """

""" #solution of positional
#it is called keyword argument

person(age=30,name='shashi')#now it does not show any error """


""" #example of bydefault argument 

person('shashi') """
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print(c)

sum(3,4,5,6)    


