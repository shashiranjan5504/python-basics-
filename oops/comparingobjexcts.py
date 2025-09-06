class computer:
    def __init__(self):
        self.name="shashi"
        self.age=24
    def compare(self,c2):
        if c1.age==c2.age:
            return True
        else:
            return False 
c1=computer()
c2=computer()

c1.age=30

if c1.compare(c2):
   print( "They are same")
else:
    print("they are not same ")
    

