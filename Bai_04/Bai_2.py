ten = input("Nhập tên học sinh : ")
Toan = float(input("Điểm toán : "))
Ly = float(input("Điểm Lý : "))
Hoa = float(input("Điểm Hóa : "))

dtb = (Toan + Ly + Hoa) / 3

if dtb >= 8:
    xeploai = "Giỏi"
elif dtb >= 6.5:
    xeploai = "Khá"
elif dtb >= 5:
    xeploai = "Trung bình"
else:
    xeploai = "Trượt"

print("=======KẾT QUẢ HỌC TẬP=======")
print("Tên học sinh : ", ten)
print("Điểm trung bình : ", round(dtb, 2))
print("Xếp loại : ", xeploai)