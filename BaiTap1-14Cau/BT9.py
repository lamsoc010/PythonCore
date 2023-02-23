import math
eps = 0.00001 #Sai số
x = float(input("Nhập x: "))
step = 2
i = 0
first = 1
second = (first - x**step / math.factorial(step+1))

while abs(first - second) > eps:
    step += 2
    i += 1
    first = second
    if (i % 2 != 0):
        second = first + x**step / math.factorial(step+1)
    else:
        second = first - x**step / math.factorial(step+1)

print("Giá trị là: ", first)