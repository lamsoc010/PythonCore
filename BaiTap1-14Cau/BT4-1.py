# Bài 4: Sai rồi
# eps = 0.00000000000000001 #Sai số
# x = float(input("Nhập x: "))
# i = 3
# step = 0
# phanTu = 1
# phanMau = 8

# first = -((phanTu/phanMau)*x**2)
# phanTu = phanTu * (i + step)
# phanMau = phanMau * (i * 2)
# second = first + ( ((phanTu / phanMau) * x ** i)) 


# # second = first + ((phanTu/phanMau)*x**i)

# while(abs(second - first) > eps): 
#     i += 1
#     step += 1
#     phanTu = phanTu * (i + step)
#     phanMau = phanMau * (i * 2)
#     first = second
#     if i % 2 == 0: 
#         second = first - ( (phanTu / phanMau) * x ** i)
#     else:
#         second = first + ( (phanTu / phanMau) * x ** i)

# result = 1 + (1/2)*x + first
# print("Giá trị là: ", result)


# Cach 2
eps = 0.00000000000000001 #Sai số
x = float(input("Nhập x: "))
i = 2
step = -1
phanTu = 1
phanMau = 2

first = (1/2)*x
phanTu = phanTu * (i + step)
phanMau = phanMau * (i * 2)
second = first - ( ((phanTu / phanMau) * x ** i)) 


# second = first + ((phanTu/phanMau)*x**i)

while(abs(second - first) > eps): 
    i += 1
    step += 1
    phanTu = phanTu * (i + step)
    phanMau = phanMau * (i * 2)
    first = second
    if i % 2 == 0: 
        second = first - ( (phanTu / phanMau) * x ** i)
    else:
        second = first + ( (phanTu / phanMau) * x ** i)

result = 1 + first
print("Giá trị là: ", result)