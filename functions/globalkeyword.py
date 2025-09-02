a=10
print(id(a))
b=11

def something():
    a=9
    
    x=globals()['a']
    print(id(x))
    print(x)
    print("in fun",a)
    globals()['a']=15

something()
print("outside",a)
