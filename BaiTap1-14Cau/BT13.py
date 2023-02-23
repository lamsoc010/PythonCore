import math
eps = 0.00001 #Sai số
x = float(input("Nhap x: "))
step = 3
first = x
second = first + x**step / math.factorial(step)

while abs(first - second) > eps:
    step += 2
    first = second
    second = first + x**step / math.factorial(step)

print("Giá trị là: ", first)