# Nhập vào 2 số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính tổng, hiệu, tích, thương của 2 số a, b. In ra màn hình kết quả . Định dạng 2 chữ số hàng thập phân
# Tính toán các giá trị
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b

# Xuất các kết quả tính toán
# : là ký tự đặc biệt để chỉ định định dạng
# .2 là sau dấu chấm làm tròn đến 2 chữ số
# f là đại diện cho kiểu dữ liệu số thực float
# .format(tong) là chèn giá trị tỏng vào trong {:.2f}
print("Tổng của a và b là: {:.2f}".format(tong))
print("Hiệu của a và b là: {:.2f}".format(hieu))
print("Tích của a và b là: {:.2f}".format(tich))
print("Thương của a và b là: {:.2f}".format(thuong))