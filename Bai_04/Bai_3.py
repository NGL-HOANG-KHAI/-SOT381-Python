nhiet_do = float(input("Nhập giá trị nhiệt độ : "))
loai = input("Nhập loại (C, F, K): ")

if loai == "C":
    F = nhiet_do * 9/5 + 32
    K = nhiet_do + 273.15
    print("F = ", round(F, 2))
    print("K = ", round(K, 2))
elif loai == "F":
    C = (nhiet_do - 32) * 5/9
    K = C + 273.15
    print("C = ", round(C, 2))
    print("K = ", round(K, 2))
elif loai == "K":
    C = nhiet_do - 273.15
    F = C + 273.15
    print("C = ", round(C, 2))
    print("F = ", round(F, 2))
else:
    print("Loại nhiệt độ không hợp lệ!!!")