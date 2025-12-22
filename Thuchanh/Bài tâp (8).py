tong  =  1
while True:
    n  = int(input("nhập số : "))
    if n >  0  and n <  10:
        for i in range(0 , n +  1):
            tong *= i
        break
    print(tong)