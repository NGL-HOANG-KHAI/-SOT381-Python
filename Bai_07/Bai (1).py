fruits = ["táo", "chuối", "cam"]

# Duyệt theo giá trị
for qua in fruits:
    print(qua)

# Duyệt theo chỉ số
for i in range(len(fruits)):
    print(f"Vị trí {i}: {fruits[i]}")

# Duyệt với enumerate
for index, value in enumerate(fruits):
    print(f"fruits[{index}] = {value}")