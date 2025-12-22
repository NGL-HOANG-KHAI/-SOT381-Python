a = int(input("Nhập số a : "))
b = int(input("Nhập số b : "))
while b != 0:
    du = a % b
    a = b
    b = du
print(f"Ước chung lớn nhất là : {b}")