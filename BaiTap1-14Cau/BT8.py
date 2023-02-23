# Bài 8
eps = 0.00001 #Sai số
x = float(input("Nhập x: "))
i = 3
first = x
phanTuTienTo = 1
phanMauTienTo = 2
second = first + ( (phanTuTienTo/phanMauTienTo) * (x**i)/i )  
while(abs(first - second) > eps):
    i += 2
    phanTuTienTo = phanTuTienTo * (i - 2)
    phanMauTienTo = phanMauTienTo * ( i - 1)

    first = second
    second = first + ( (phanTuTienTo/phanMauTienTo) * (x**i)/i )   

print("Giá trị là: ", first)