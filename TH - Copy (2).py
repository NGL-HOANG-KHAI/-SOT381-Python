n = int(input("Nhập số mà bạn muốn : "))
if n <= 100 and n >= 1 :
    if n % 3 == 0 and n % 5 == 0:
        print("Số thỏa mãn 2 điều kiện ")
    else:
        print("Không thỏa")
    