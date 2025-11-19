a = float(input("Nhập số a : "))
b = float(input("Nhập số b : "))
c = float(input("Nhập số c : "))

if a + b > c and a + c > b and c + b > a:
    print("Tam giác hợp lệ")
else:
    print("Tam giác không hợp lệ !!!")