
#example of no inheritance 
class A:
    def feature1(self):
        print("feature 1 is working ")
    def feature2(Self):
        print("feature 2 is working ")
class B:
    def feature3(self):
        print("feature 3 is working ")
    def feature4(Self):
        print("feature 4 is working ")

a1=A()
a1.feature1()


b1=B()
b1.feature3()  #here if b do not inherit calls a it cannot use feature 1 and feature 2






    