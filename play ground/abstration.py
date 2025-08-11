from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def are(self):
        pass
    @abstractmethod
    def perimeter (self):
        pass

class Square(Shape):
    def __init__(self,side):
        self,side = side

    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4 *self.length

sq_1 = Square(4) 
print(sq_1.side)