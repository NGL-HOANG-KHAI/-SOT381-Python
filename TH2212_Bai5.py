def tinh_S(n):
    TS = 0
    for i in range(1 , n):
        TS += i

    MS = 0
    for i in range(2 , n//2 + 1):
        MS = MS + 2*i
    S = TS / MS
    return S
n = int(input("Nhập số n : "))
kq = tinh_S(n)
print(f"Kết quả S = {kq}")    
        