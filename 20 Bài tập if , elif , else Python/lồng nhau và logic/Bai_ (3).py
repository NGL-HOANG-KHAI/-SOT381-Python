a = float(input("Nhập số  : "))
b = float(input("Nhập số  : "))
op = input("Nhập dấu mà bạn muôn (+, - , * , /) : ")

if op == "+":
    print("Đáp án : ", a + b)
elif op == "-":
    print("Đáp án : ", a - b)
elif op == "*":
    print("Đáp án : ", a * b)
elif op == "/":
    if b == 0:
        print("Lỗi đáp án ")
    else:
        print("Đáp án : ", a/b)
