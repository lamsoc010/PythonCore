
import math
# Bài 2
# eps = 0.00001 #Sai số
# i = 1 
# x = float(input("Nhập x: "))

# first = 1
# second = first - ( (((i+1) * (i+2))/2)*x**i )

# while(abs(first - second) > eps):
#     i += 1
#     first = second 

#     if(i % 2 == 0): 
#         second = first + ( (((i+1) * (i+2))/2)*x**i )
#     else:
#         second = first - ( (((i+1) * (i+2))/2)*x**i )

# print("Giá trị là:", first)

# Bài 3:
# eps = 0.00001 #Sai số
# x = float(input("Nhập x: "))
# i = 2
# first = -x
# second = first - ((x**i)/i)

# while(abs(first - second) > eps):
#     i += 1
#     first = second 
#     second = first - ((x**i)/i)
# print("Giá trị là: ", first)

# Bài 4: Sai rồi
eps = 0.000001 #Sai số
x = float(input("Nhập x: "))
i = 1
first = 1
second = first + ((1/2)*x**i)

phanTu = 1
phanMau = 2

while(abs(first - second) > eps): 
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

# Bài 5:
# eps = 0.00001 #Sai số
# x = float(input("Nhập x: "))
# i = 0
# first = 1
# second = first - ((1/2)*x**(i+1))

# phanTu = 1
# phanMau = 2
# soMu = 1
# while(abs(first - second) > eps): 
#     i += 2
#     soMu += 1
#     phanTu = phanTu * (i + 1)
#     phanMau = phanMau * (i + 2)
#     first = second
#     if soMu % 2 == 0:
#         second = first + ((phanTu / phanMau) * x**soMu)
#     else:
#         second = first - ((phanTu / phanMau) * x**soMu)
# print("Giá trị là: ", first)

# Bài 6:

# eps = 0.00001 #Sai số
# x = float(input("Nhập x: "))
# i = 3
# first = x
# second = first - ( (x**i)/math.factorial(i) )
# checkEven = 1
# while(abs(first - second) > eps):
#     i += 2
#     checkEven += 1
#     first = second
#     if checkEven % 2 == 0:
#         second = first + ( (x**i)/math.factorial(i) )
#     else:
#         second = first - ( (x**i)/math.factorial(i) )    

# print("Giá trị là: ", first)

# Bài 7
# eps = 0.00001 #Sai số
# x = float(input("Nhập x: "))
# i = 2
# first = 1
# second = first - ( (x**i)/math.factorial(i) )
# checkEven = 1
# while(abs(first - second) > eps):
#     i += 2
#     checkEven += 1
#     first = second
#     if checkEven % 2 == 0:
#         second = first + ( (x**i)/math.factorial(i) )
#     else:
#         second = first - ( (x**i)/math.factorial(i) )    

# print("Giá trị là: ", first)

# Bài 8
# eps = 0.00001 #Sai số
# x = float(input("Nhập x: "))
# i = 3
# first = x
# phanTuTienTo = 1
# phanMauTienTo = 2
# second = first + ( (phanTuTienTo/phanMauTienTo) * (x**i)/i )  
# while(abs(first - second) > eps):
#     i += 2
#     phanTuTienTo = phanTuTienTo * (i - 2)
#     phanMauTienTo = phanMauTienTo * ( i - 1)

#     first = second
#     second = first + ( (phanTuTienTo/phanMauTienTo) * (x**i)/i )   

# print("Giá trị là: ", first)