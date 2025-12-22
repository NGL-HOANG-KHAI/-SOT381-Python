def sln(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


def snn(a,b,c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min
a = int(input("Nhập số a : "))
b = int(input("Nhập số b : "))
c = int(input("Nhập số c : "))
numMin = snn(a,b,c)
numMax = sln(a,b,c)
print(f"Số nhỏ nhất {numMin}")
print(f"Số lớn nhất {numMax}")
