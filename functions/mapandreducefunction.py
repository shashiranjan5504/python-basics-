from functools import reduce

def update (n):
    return n*2
def add_all(a,b):
    return a+b
nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(update,evens))
doubles=list(map(lambda n:n*2,evens))#use of lamda function
print(doubles)

sum=reduce(add_all,doubles)#use of lamda function 

print(sum)
