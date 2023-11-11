# 40
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if (a>0) and (b>0) and (c>0) and (a+b>c) and (b+c>a) and (a+c>b):
 if a==b==c :
    print('Tam giác đều')
 elif a!=b and b!=c and a!=c :
    print('Tam giác thường')
 else :
    print('Tam giác cân')
else :
    print('Khong phai tam giac')