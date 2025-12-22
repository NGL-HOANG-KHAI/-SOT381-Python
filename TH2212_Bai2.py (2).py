a = int(input("Nhập số a : "))
b = int(input("Nhập số b :"))
c = int(input("Nhập số c : "))

max = a
if b > max :
    max = b
if c > max :
    max = c
print(f"Số lớn nhất :  {max}" )

min = a
if b < min :
    min = b
if c < min :
    min = c
print(f"Số nhỏ nhất :  {min}" )
