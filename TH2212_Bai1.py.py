while True:
    d = float(input("Nhập chiều dài : "))
    r = float(input("Nhập chiều rộng : "))
    chu_vi = (d + r) * 2
    dien_tich = d * r
    if 0.0 <= d and r <= 100:
        print(f"{chu_vi:.2f}")
        print(f"{dien_tich:.2f}")
    else:
        print("Sai rồi")