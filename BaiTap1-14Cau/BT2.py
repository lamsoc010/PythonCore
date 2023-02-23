# Bài 2
eps = 0.00001 #Sai số
i = 1 
x = float(input("Nhập x: "))

first = 1
second = first - ( (((i+1) * (i+2))/2)*x**i )

while(abs(first - second) > eps):
    i += 1
    first = second 

    if(i % 2 == 0): 
        second = first + ( (((i+1) * (i+2))/2)*x**i )
    else:
        second = first - ( (((i+1) * (i+2))/2)*x**i )
        
print("Giá trị là:", first)
