class  student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
        lap1.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.__dict__)
        


s1=student('navin',2)
s2=student('jenny',3)
lap1=s1.lap
print(s1.lap.ram)
 

s1.show() 
