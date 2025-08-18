a=5
b=6
""" method 1
temp =a
a=b
b= temp
print(a)
print(b)
 """
""" method 2
a=a+b
b=a-b
a=a-b
print(a)
print(b) """

# method 3 (behind t he scene  it uses the concept of two rotation )
a,b=b,a
print(a)
print(b)
