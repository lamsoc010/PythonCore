# Bài 3:
eps = 0.00001 #Sai số
x = float(input("Nhập x: "))
i = 2
first = -x
second = first - ((x**i)/i)

while(abs(first - second) > eps):
    i += 1
    first = second 
    second = first - ((x**i)/i)
print("Giá trị là: ", first)