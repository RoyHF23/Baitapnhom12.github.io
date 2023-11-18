#72
s=input("Nhap chuoi:")
x=''
for i in s:
    x=i+x
if x==s:
    print(s,'la chuoi Palindrome')
else:
    print(s,'khong la chuoi Palindrome')