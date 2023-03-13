# pip install wheel
# pip install pandas
# pip install openpyxl
import pandas as pd


class Student:
    def __init__(self, maSV, hoTen, ngaySinh, khoa, nganh, lop, nienKhoa, anhThe):
        self.maSV = maSV
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.khoa = khoa
        self.nganh = nganh
        self.lop = lop
        self.nienKhoa = nienKhoa
        self.anhThe = anhThe
        # self.xepLoai = self.xepLoaiHocLuc()
# đọc file excel


def readExcel(url):
    # đọc file excel
    # skiprows: bỏ qua n dòng đầu tiên
    # nrows: chỉ đọc n dòng
    # usecols: chỉ đọc cột 1 => 8
    # iloc[a, b] a: hàng, b: cột
    require_cols = [1, 2, 3, 4, 5, 6, 7, 8]
    dataframe1 = pd.read_excel(
        url,  skiprows=1, nrows=20, usecols=require_cols)
    listStudent = []
    for i in range(len(dataframe1)):
        sv = Student(dataframe1.iloc[i, 0], dataframe1.iloc[i, 1], dataframe1.iloc[i, 2], dataframe1.iloc[i, 3],
                     dataframe1.iloc[i, 4], dataframe1.iloc[i, 5], dataframe1.iloc[i, 6], dataframe1.iloc[i, 7])
        listStudent.append(sv)
    return listStudent



# listStudent = SortListStudent(listStudent)
# printListStudent(listStudent)
# statistical(listStudent)