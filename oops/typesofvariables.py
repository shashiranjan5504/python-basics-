class car :

    wheels=4
    def __init__(self):
        self.mil=10

        self.com="BMW"
c1=car()
c2=car()
car.wheels=5

print(c2.__dict__,c2.wheels)#dict on;y print the 
print(c2.__dict__,c2.wheels)







        