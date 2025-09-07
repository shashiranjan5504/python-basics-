from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        pass
class Rectangle(shape):
    types="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7
"""   def printarea(self):
        return self.length*self.breadth  """
rec1=Rectangle()
print(rec1.printarea())