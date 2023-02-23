import math
eps = 0.00001 #Sai số
x = float(input("Nhap x: "))
step = 3
i = 0
first = x
second = (first - x**step / step)

while abs(first - second) > eps:
    step += 2
    i += 1
    first = second
    if (i % 2 != 0):
        second = first + x**step / step
    else:
        second = first - x**step / step

print("Giá trị là: ", first)