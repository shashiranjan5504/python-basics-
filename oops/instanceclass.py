

#instance method

class student :
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):#accessors or getters
        return self.m1
    def set_m1(self,value):#mutators or setters
        self.m1=value


s1=student(34,47,32)
s2=student(89,32,12)
s3=student()#it gives an error as the constructor is not called as the init  method require three positional argument .  
print(s1.avg())
print(s2.avg())
#print(s3.__dict__)




    