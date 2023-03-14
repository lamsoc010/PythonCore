from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        

    @abstractmethod
    def chuVi(self):
        pass

    @abstractmethod
    def dienTich(self):
        pass

    @abstractmethod
    def viTri(self):
        pass
    

