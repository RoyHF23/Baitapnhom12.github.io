# Bài tập 78: Chuyển đổi từ thập phân sang nhị phân
q = int(input("Nhập số thập phân cần chuyển đổi: "))
result = ""
while q != 0:
    r = q % 2
    result = str(r) + result
    q //= 2
print("Biểu diễn nhị phân của số là:", result)