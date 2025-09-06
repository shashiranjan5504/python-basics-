class computer:
    def __init__(self,cpu,ram):#it is a python constructor
        self.cpu=cpu
        self.ram=ram
        
    def config(self):
        print("configuration is :",self.cpu,self.ram)

com1=computer('i5',16)
com2=computer('ryzen 5',32)

com1.config()
com2.config()