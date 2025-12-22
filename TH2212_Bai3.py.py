def sln(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max
a = 3
b = 2
c = 7
numMax = sln(a,b,c)
print(f"Số lớn nhất {numMax}")

def snn(m,n,k):
    min = m
    if n < min:
        min = n
    if k < min:
        min = k
    return min
m = 1
n = 2
k = 3
numMin = snn(m,n,k)
print(f"Số nhỏ nhất {numMin}")