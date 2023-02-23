# Bài 5:
eps = 0.00001 #Sai số
x = float(input("Nhập x: "))
i = 0
first = 1
second = first - ((1/2)*x**(i+1))

phanTu = 1
phanMau = 2
soMu = 1
while(abs(first - second) > eps): 
    i += 2
    soMu += 1
    phanTu = phanTu * (i + 1)
    phanMau = phanMau * (i + 2)
    first = second
    if soMu % 2 == 0:
        second = first + ((phanTu / phanMau) * x**soMu)
    else:
        second = first - ((phanTu / phanMau) * x**soMu)
print("Giá trị là: ", first)