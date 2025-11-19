a = float(input("Vui lòng nhập số : "))
b = float(input("Vui lòng nhập số : "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm ")
    if b != 0:
        print("Phương trình vô nghiệm ") 
else:
    x = -b/a
    print("Phương trình có 1 nghiệm ")
