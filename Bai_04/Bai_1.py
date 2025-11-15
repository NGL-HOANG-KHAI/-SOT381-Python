so = int(input("Nhập số điện đã dùng : "))
tien = 0
if so <= 50:
    tien = so * 1678
elif so <= 100:
    tien = 50 * 1678 + (so - 50) * 1734
elif so <= 200:
    tien = 50 * 1678 + 50 * 1734 + (so - 100) * 2014
elif so <= 350:
    tien = 50 * 1678 + 50 * 1734 + 50 * 2014 + (so - 200) * 2536
else:
    tien = 50 * 1678 + 50 * 1734 + 50 * 2014 + 50 * 2536 + (so - 350) * 2927

print("Tiền điện phải trả là : " , tien, "VND")