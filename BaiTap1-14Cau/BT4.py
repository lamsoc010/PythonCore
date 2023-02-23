# Bài 4: Sai rồi
eps = 0.00000000000001 #Sai số
x = float(input("Nhập x: "))
i = 1
first = 1

phanTu = 1
phanMau = 2

second = first + ((phanTu/phanMau)*x**i)

while(abs(second - first) > eps): 
    i += 1
    if(i % 2 != 0): 
        phanTu = phanTu * i
    phanMau = phanMau * (i * 2)
    first = second
    if i % 2 == 0:
        second = first - ((phanTu / phanMau) * x**i)
    else:
        second = first + ((phanTu / phanMau) * x**i)
print("Giá trị là: ", first)