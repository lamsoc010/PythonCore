import readFileExcel
import createStudentCard

url = 'D:\\Study\\DHPhuXuan\\Nam3\\HK-Spring\\Python\\TheSinhVien\\assets\\input\\danhsachsinhvien.xlsx'

listStudent = readFileExcel.readExcel(url)
# In ra danh sách sinh viên với các thông tin cần thiết
for i, student in enumerate(listStudent, start=1):
    createStudentCard.renderStudentCard(student, i)
