# 35
n=float(input("Nam con nguoi:"))
if  (n<0):
    print("Khong hop le")
elif n<=2:
      print("Tuoi con cho la:",n*10.5)
elif (n>2):
      print("Tuoi con cho la:",(2*10.5)+((n-2)*4))