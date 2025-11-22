von = int(input("Nhập số vốn : "))
nam = int(input("Nhập số năm : "))
lai_suat = int(input("Nhập lãi suất : "))

print(f"đầu tư {von : .0f} VND với lãi suất {lai_suat  : .0f}")
for i in range(1 , nam + 1):
    von = von * (lai_suat + 1)
    print(f"nam {i} : {von : .0f} VND")
print(f"sau {nam} năm : von {von : .0f}VND")