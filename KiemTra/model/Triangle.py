from model.Shape import Shape
import math

class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x,y)
        self.a = a
        self.b = b
        self.c = c
        
    def chuVi(self):
        return self.a + self.b + self.c

    def dienTich(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def viTri(self):
        return (self.x, self.y)
    
    def __str__(self):
        return f"Hình tam giác có 3 cạnh a, b, c tương ứng {self.a}, {self.b}, {self.c}, x: {self.x}, y: {self.y}"