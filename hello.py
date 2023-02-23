# Khai báo biến
hoTen = "Tran Vinh Lam"
namSinh = 1999

# Một Object 
thongTin = {
    "soDo": [85,70,100],
    "chieuCao": 1.65,
    "canNang": 68
}
print("Họ tên: " + hoTen)
print(thongTin['chieuCao'])

# Câu điều kiện
namHienTai = 2021
if namHienTai - namSinh > 20:
    print("Da nghi huu")
else:
    print("Vang dang cay")
    
# Vòng lặp(range là khoảng lặp trong python)
for n in range(1,10): 
    print(namHienTai)
    namHienTai = namHienTai+1

# Lặp qua mảng
for duLieu in thongTin['soDo']:
    print(duLieu)

# Khai báo hàm
def boiTinhDuyen(tenNam, tenNu):
    #Tinh Toan
    tenNam = tenNam.lower()
    tenNu = tenNu.lower()
    # ord chuyển đổi chữ cái thành số
    dem = 0
    for chuCai in range(ord('a'), ord('z') + 1):
        if (chr(chuCai) in tenNam) and (chr(chuCai) in tenNu):
            dem = dem + 1
    if dem == 0:
        return "Nguoi dung nuoc la"
    elif dem < 3:
        return "Cung duoc day"
    else:
        return "Toi luon de ban oi"
        # chr chuyển đổi số thành chữ cái
        
# Nhập từ bàn phím
print("Nhap ten Nam: ")
tenNam = input()

print("Nhap ten Nu: ")
tenNu = input()

# Gọi hàm
print(boiTinhDuyen(tenNam, tenNu)) 
    
    
    
    
    
    
    
    
    
    