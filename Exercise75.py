# Ước chung lớn nhất
n=int(input("Nhập số nguyên dương thứ nhất: "))
m=int(input("Nhập số nguyên dương thứ hai: "))
d = min(n, m)
if n > 0 and m > 0:   
  while d>=1 :
   if n % d == 0 and m % d == 0:
    print(f"Ước số chung lớn nhất của {n} và {m} là: {d}") 
    break
   d-=1
else :
   print("Vui lòng nhập hai số nguyên dương.")