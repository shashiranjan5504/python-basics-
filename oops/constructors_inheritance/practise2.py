
#EXAMPLE OF METHOD RESOLUTION ORDER
class A:
    def __init__(self):
        print("init a")
    def feature1(self):
        print("feature 1-A is working ")
    def feature2(Self):
        print("feature 2 is working ")
class B:
    def __init__(self):
        print("init b")
    def feature1(self):
        print("feature 1-B is working ")
    def feature4(Self):
        print("feature 4 is working ")


class C(B,A):
    def __init__(self):
        print("init c")
        super().__init__()
    def feature5(self):

        print("feature  5 is working ")
c1=C()
c1.feature1()


