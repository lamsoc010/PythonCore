import model.Rect as rect
import model.Circle as circle
import model.Triangle as triangle

def readRectangles(file_name):
    rectangles = []
    circles = []
    triangles = []
    with open(file_name) as f:
        for line in f:
            if line.startswith('#Rect'):
                # đọc thông tin hình chữ nhật
                chieuDai, chieuRong = map(int, f.readline().split())
                x, y = map(int, f.readline().split())
                rectangle = rect.Rect(x, y, chieuDai, chieuRong)
                rectangles.append(rectangle)
            if line.startswith('#Circle'):
                # đọc thông tin hình tròn
                banKinh = int(f.readline())
                x, y = map(int, f.readline().split())
                circle1 = circle.Circle(x, y, banKinh)
                circles.append(circle1)
            if line.startswith('#Triangle'):
                # đọc thông tin hình tam giác
                a, b, c = map(int, f.readline().split())
                x, y = map(int, f.readline().split())
                triangle1 = triangle.Triangle(x, y, a, b, c)
                triangles.append(triangle1)   
    return rectangles, circles, triangles