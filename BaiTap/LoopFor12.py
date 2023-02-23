# 11.1 Viế t chương trì nh tí nh tổ ng cá c số từ 1 đế n 100
def tinhTong():
    tong = 0
    for i in range(0, 101):
        tong = tong + i
    return tong

print("Tổng từ 1 đến 100 là: ", tinhTong())

# 11.2 Viế t chương tì nh nhậ p và o mộ t số tự nhiên n. Tí nh tổ ng cá c số chia hế t cho 3 bé hơn n
def tongCacSoChiaHetCho3BeHonN(n):
    tong = 0
    for i in range(0, n):
        print(i)
        if i % 3 == 0:
            tong = tong + i
    return tong
n = int(input("Nhập n: "))
print("Tổng các số chia hết cho 3 nhỏ hơn", n, "là:", tongCacSoChiaHetCho3BeHonN(n))

# 11.3 Viế t chương trì nh in ra 100 số Fibonacci đầ u tiên.
def soFibonacci():
    a = 0
    b = 1
    for i in range(0, 100): 
        print(a)
        c = a
        a = b
        b = c + b
# soFibonacci()

# 11.4 Viế t chương trì nh kiể m tra mộ t số nguyên n có phả i là số polinom (số polinom là số đả o ngượ c đả o xuôi là mộ t. Ví dụ : 1256521), n nhậ p và o từ bà n phí m
def kiemTraSoPolinom(n): 
    # Lưu số ban đầu vào một biến khác
    num = n

    # Khởi tạo biến reverse_num
    reverse_num = 0

    # Tìm số đảo ngược của số ban đầu
    while n > 0:
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n = n // 10

    # Kiểm tra số đối xứng
    if num == reverse_num:
        print(num, "là số đối xứng")
    else:
        print(num, "không phải là số đối xứng")

n = int(input("Nhập một số nguyên dương: "))

kiemTraSoPolinom(n)


# 11.5 Viế t chương trì nh liệ t kê cá c số từ 100 đế n 999 có tổ ng cá c chữ số chia hế t cho 3.
def tongCacSoTu100Den999CoTongCacChuSoChiaHetCho3() :
    for i in range(100, 1000):
        # Vd 123 
        # sum_digits = (123//100) + (123 // 10 % 10) + (123 % 10) = 1 + (12 % 10) + 3 = 1 + 2 + 3
        sum_digits = (i // 100) + (i // 10 % 10) + (i % 10)
        if sum_digits % 3 == 0:
            print(i)
