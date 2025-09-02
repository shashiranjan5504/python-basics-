def fact(n):
    product=1
    for i in range(n,n>0,-1):
        product =product*i
    return product
factorial=fact((int(input("enter the value of numnber "))))
print(factorial) 
