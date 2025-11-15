n = int(input("Nhập số liệu cần kiểm tra : "))
la_chan = (n % 2 == 0)
lon_hon_10 = (n > 10)
chia_het_cho_3 = (n % 3 == 0)
if la_chan and lon_hon_10 and chia_het_cho_3:
    print("Số thỏa mãn cả 3 điều kiện")
else:
    print("Không thỏa mãn cả 3 điều kiện!!!")
