#68
n=input("Nhap 8 bit:")
while (n!=''):
    if (n.count("0")+n.count("1")!=8) or (len(n)!=8):
        print("khong hop le")
    else:
        x=n.count("1")
        if (x%2==0):
          print("Bit chan le la 0")
        else:
          print("Bit chan le la 1")
    n=input("Nhap 8 bit:")