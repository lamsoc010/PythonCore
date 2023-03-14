import lib.readFileInput as readFile
import lib.renderFileInput as writeFile
import model.Rect as rect
import lib.checkOverlapping as checkOverlapping

class Main():
    def __init__(self):
        self.listRectObject = []
        self.listCircleObject = []
        self.listTriangleObject = []
        pass

    def writeToFile(self, fileName, totalRecords):
        writeFile.generate_input_file(fileName, totalRecords)

    def readFromFile(self, fileName):
        self.listRectObject, self.listCircleObject, self.listTriangleObject = readFile.readRectangles(fileName)
        
    
    def chuViLonNhat(self):
        maxChuVi = maxDienTich = 0
        hinhCoChuViLonNhat = hinhCoDienTichLonNhat = None

        # Duyệt qua từng hình trong 3 list rectangles, circles, triangles.
        for shape in self.listRectObject + self.listCircleObject + self.listTriangleObject:
            chuVi = shape.chuVi()
            dienTich = shape.dienTich()

            # So sánh giá trị chu vi và diện tích tính được với giá trị chu vi lớn nhất và diện tích lớn nhất hiện tại.
            if chuVi > maxChuVi:
                maxChuVi = chuVi
                hinhCoChuViLonNhat = shape

            if dienTich > maxDienTich:
                maxDienTich = dienTich
                hinhCoDienTichLonNhat = shape

        return hinhCoChuViLonNhat, hinhCoDienTichLonNhat
         
    def checkOverlapping(self):
        max_count, max_overlapping_shapes = checkOverlapping.count_overlapping_shapes(self.listRectObject + self.listCircleObject + self.listTriangleObject)
        return max_count

object = Main()
fileName = "input.txt"
totalRecords = 10
# Tự động render dữ liệu vào file input
# object.writeToFile(fileName, totalRecords)
# Câu 4a: Đọc dữ liệu từ file input
object.readFromFile(fileName)

# Câu 4b: Liệt kê hình có chu vi và diện tích lớn nhất
hinhCoChuViLonNhat, hinhCoDienTichLonNhat = object.chuViLonNhat()
print(f"Hình có diện tích lớn nhất là: {hinhCoChuViLonNhat.__str__()} với diện tích: {hinhCoChuViLonNhat.dienTich()}")
print(f"Hình có chu vi lớn nhất là: {hinhCoDienTichLonNhat.__str__()} với chu vi: {hinhCoDienTichLonNhat.chuVi()}")

# Câu 4c:
# print(object.checkOverlapping())


