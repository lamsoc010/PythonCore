from model.Shape import Shape
import math

class Circle(Shape):
    def __init__(self, x, y, banKinh):
        super().__init__(x,y)
        self.banKinh = banKinh
    
    def chuVi(self):
        return 2 * math.pi * self.banKinh

    def dienTich(self):
        return math.pi * self.banKinh ** 2

    def viTri(self):
        return (self.x, self.y)
        
    def __str__(self):
        return f"Hình tròn: bán kính {self.banKinh}, x: {self.x}, y: {self.y}"
