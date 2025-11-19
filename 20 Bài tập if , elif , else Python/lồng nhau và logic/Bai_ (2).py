a = float(input("Vui lòng nhập số a : "))
b = float(input("Vui lòng nhập số b : "))
c = float(input("Vui lòng nhập số c : "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        print("Có nghiệm kép")
    else:
        print("Có 2 nghiệm phân biệt")