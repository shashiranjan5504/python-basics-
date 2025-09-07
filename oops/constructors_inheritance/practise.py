class A:
    def __init__(self):
        print("init a")
    def feature1(self):
        print("feature 1 is working ")
    def feature2(Self):
        print("feature 2 is working ")
class B(A):
    def __init__(self):
        print("init b")
        super().__init__()
    def feature3(self):
        print("feature 3 is working ")
    def feature4(Self):
        print("feature 4 is working ")
class C(B):
    """ def __init__(self):
        print("init c")
        super().__init__() """
    def feature5():
        print("feature 5 is working ")


b1=C()


