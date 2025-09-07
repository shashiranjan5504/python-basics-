class  student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
        
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

lap1=student.Laptop()

print(lap1.brand)