
a = float(input("điểm Toán : "))
b = float(input("điểm Lý : "))
c = float(input("điểm Hóa : "))
diem_tong = (a + b + c) 
if diem_tong >= 15 and diem_tong != 4 :
    print("Đậu")
    if a > 5 and b > 5 and c > 5:
        print("Học đều các môn")
    else:
        print("Học chưa đều các môn")
else:

    print("Thi hỏng")
