class  student:#outer class
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        


s1=student('navin',2)
s2=student('jenny',3)
s1.show()  
print(s1.lap.brand)   
lap1=s1.lap
lap2=s2.lap

print(lap1.ram)


