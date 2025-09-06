class computer:
    def __init__(self):
        self.name="shashi"
        self.age=24
    def update(self):
        self.age=30
c1=computer()
c2=computer()
c1.name="rashi"

#print(id(c1))#
#print(id(c2 ))



print(c1.__dict__)
print(c2.__dict__)
c1.update()# here it expalin why self is important    
print(c1.__dict__)
print(c2.__dict__)
