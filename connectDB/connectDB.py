import mysql.connector
import readFileExcel
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

# Tạo bảng
mycursor = mydb.cursor()
def createTable() :
    mycursor.execute("CREATE TABLE Student (STT INT AUTO_INCREMENT PRIMARY KEY, maSV VARCHAR(255), ho VARCHAR(255), ten VARCHAR(255), ngaySinh DATE, diemToan FLOAT, diemLy FLOAT, diemHoa FLOAT)")
# CRUD
def read() :
    mycursor.execute("SELECT * FROM artist")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# createTable()
# Insert list Students
url = 'D:\\Study\\DHPhuXuan\\Nam3\\HK-Spring\\Python\\BaiTap2\\input.xlsx'
listStudents = readFileExcel.readExcel(url)

def insert(student):
    sql = "INSERT INTO Student (maSV, ho, ten, ngaySinh, diemToan, diemLy, diemHoa) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    val = (student.maSV, student.ho, student.ten, datetime.strptime(student.ngaySinh, '%d/%m/%Y'), student.mToan, student.mLy, student.mHoa)
    mycursor.execute(sql, val)

    # Lưu thay đổi vào cơ sở dữ liệu
    mydb.commit()

for student in listStudents:
    print(student.maSV)
    print(student.ho)
    print(student.ten)
    print(student.ngaySinh)
    print(student.mToan)
    print(student.mLy)
    print(student.mHoa)
    insert(student)

