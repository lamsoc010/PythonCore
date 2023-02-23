# 9.1 Viết chương trình nhập vào một số nguyên. Kiểm tra số đó nguyên dương hay nguyên âm. In ra mà n hì nh kế t quả
# a = int(input("Nhập số nguyên a: "))
# if a > 0:
#     print("{} là số nguyên dương".format(a))
# elif a < 0:
#     print(a, "là số nguyên âm")
# else:
#     print(a, "bằng 0")

# -----------------------------------------------------------------------------------------
# 9.2 Viế t chương trì nh nhậ p và o mộ t số nguyên n. Kiểm tra n chia hết cho 3 hay 5. In kế t quả ra mà n hì nh
# n = int(input("Nhập số nguyên n: "))
# if (n % 3 == 0) and (n % 5 == 0):
#     print(n, "vừa chia hết cho 3 vừa chia hết cho 5")
# elif n % 3 == 0:
#     print(n, "chia hết cho 3")
# elif n % 5 == 0:
#     print(n, "chia hết cho 5")
# else:
#     print(n, "không chia hết cho 3 và cũng không chia hết 5")

# -----------------------------------------------------------------------------------------
# 9.3 Viế t chương trì nh nhậ p và o thá ng trong năm. In ra sốngà y củ a tháng đó
# thang = int(input("Nhập vào một tháng trong năm: "))

# if thang == 2:
#     nam = int(input("Nhập năm: "))
#     # Kiểm tra năm đó có nhuận hay không
#     if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
#         ngay = 29
#     else:
#         ngay = 28
# elif thang in [4, 6, 9, 11]:
#     ngay = 30
# else:
#     ngay = 31

# print("Tháng", thang, "có", ngay, "ngày")

# -----------------------------------------------------------------------------------------

# 9.4 Viế t chương trì nh giả i phương trì nh bậ c 2
# ax^2 + bx + c
# import math
# a = float(input("Nhập a: "))
# b = float(input("Nhập b: "))
# c = float(input("Nhập c: "))

# # Tính delta
# delta = b**2 - 4*a*c

# # Kiểm tra giá trị của delta
# if delta > 0:
#     x1 = (-b + math.sqrt(delta)) / (2*a)
#     x2 = (-b - math.sqrt(delta)) / (2*a)
#     print("Phương trình có hai nghiệm phân biệt: x1 =", x1, "và x2 =", x2)
# elif delta == 0:
#     x = -b / (2*a)
#     print("Phương trình có nghiệm kép: x =", x)
# else:
#     print("Phương trình vô nghiệm")

# -----------------------------------------------------------------------------------------
# 9.5 Viế t chương trì nh nhậ p và o 3 số a, b, c. Kiể m tra có phả ilà 3 cạ nh củ a mộ t tam giá c không?
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện của tam giác
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Ba số", a, ",", b, "và", c, "là 3 cạnh của một tam giác")
else:
    print("Ba số", a, ",", b, "và", c, "không phải là 3 cạnh của một tam giác")