#73
s= input("Nhap chuoi:")
s=s.replace(" ","")
is_palindrome = True
i=0
while i < len(s) / 2 and is_palindrome :
  if s[i] != s[len(s) - i - 1]:
     is_palindrome = False
  i=i+1
if is_palindrome:
     print("La chuoi palindrome")
else:
     print("Khong la chuoi palindrome")