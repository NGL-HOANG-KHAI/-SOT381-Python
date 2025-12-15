n = int(input("Nhập n: "))

tong = 0  # biến để lưu tổng

for i in range(1, n + 1):   # chạy từ 1 đến n
    tong = tong + i         # cộng dồn vào tổng

print("Tổng từ 1 đến", n, "là:", tong)