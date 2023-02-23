# Bài 7
import math
eps = 0.00001 #Sai số
x = float(input("Nhập x: "))
i = 2
first = 1
second = first - ( (x**i)/math.factorial(i) )
checkEven = 1
while(abs(first - second) > eps):
    i += 2
    checkEven += 1
    first = second
    if checkEven % 2 == 0:
        second = first + ( (x**i)/math.factorial(i) )
    else:
        second = first - ( (x**i)/math.factorial(i) )    

print("Giá trị là: ", first)