a = float(input("Nhập số a : "))
b = float(input("Nhập số b : "))
c = float(input("Nhập số c : "))

if a + b > c and a + c > b and c + b > a:
    print("Tam giác hợp lệ")
    if a == b == c:
        print("Tam giác đều")
    elif a == b >= c or a == c >= b or c == b >= a:
        print("Tma giác cân")
    elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("Tam giác vuông")
    else:
        print("Tma giác thường")
else:
    print("Tam giác không hợp lệ")