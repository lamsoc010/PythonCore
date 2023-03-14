from model.Shape import Shape

class Rect(Shape):
    def __init__(self, x, y, chieuDai, chieuRong):
        super().__init__(x,y)
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong 
    
    def chuVi(self):
        return 2 * (self.chieuDai + self.chieuRong)

    def dienTich(self):
        return self.chieuDai * self.chieuRong

    def viTri(self):
        return (self.x, self.y)
    
    def __str__(self):
        return f"Hình chữ nhật có chiều dài: {self.chieuDai} và chiều rộng: {self.chieuRong}, x: {self.x}, y: {self.y}"
