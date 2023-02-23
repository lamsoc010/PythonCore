# Viế t chương trì nh nhậ p và o mộ t mả ng 10 phầ n tử số nguyên
listInteger = []
for i in range(0, 10):
    listInteger.append(int(input("Nhập phần tử thứ {} là một số nguyên vào mảng: ".format(i + 1))))

# In mảng ra màn hình
for i in listInteger:
    print(i)

# 1. Tí nh tổ ng cá c phầ n tử củ a mả ng. Kiể m tra tổ ng là chẵ n hay lẻ . In kế t quả ra mà n hì nh
def tinhTong():
    tong = 0
    for i in listInteger:
        tong += i
    return tong
print("Tổng các phần tử trong mảng: ", tinhTong())

# 2. Kiể m tra mả ng có bao nhiêu số chẵ n, bao nhiêu số lẻ . In kế t quả ra mà n hì nh
def kiemTraChanLe():
    soSoChan = 0
    soSoLe = 0
    for i in listInteger:
        if i % 2 == 0:
            soSoChan += 1
        else:
            soSoLe += 1
    print("Số số chẵn trong mảng là: ", soSoChan)
    print("Số số lẻ trong mảng là: ", soSoLe)
kiemTraChanLe()

# 3. ắ p xế p cá c phầ n tử mả ng theo thứ tự tăng dầ n, giả m dầ n. In mả ng ra mà n hì nh.
# Sắp xếp tăng dần
listInteger.sort()
print("Mảng sắp xếp theo thứ tự tăng dần:", listInteger)

# Sắp xếp giảm dần
listInteger.sort(reverse=True)
print("Mảng sắp xếp theo thứ tự giảm dần:", listInteger)

# 4. Kiể m tra có bao nhiêu số nguyên tố xuấ t hiệ n trong mả ng
def demSoNguyenToTrongMang():
    soSoNguyenTo = 0
    for i in listInteger:
        if i > 2:
            dem = 0
            for j in range(2, int(i**0.5)+1):
                if(i % j == 0):
                    dem = dem + 1
                    break
            if(dem == 0):
                soSoNguyenTo = soSoNguyenTo + 1
    return soSoNguyenTo
print("Số số nguyên tố trong mảng là: ", demSoNguyenToTrongMang())

