#42
n=float(input("Tan so:"))
if abs(n-261.63)<=1:
    print("C")
elif abs(n-293.66)<=1:
    print("D")
elif abs(n-329.63)<=1:
    print("E")
elif abs(n-349.23)<=1:
    print("F")
elif abs(n-392.00)<=1:
    print("G")
elif abs(n-440.00)<=1:
    print("A")
elif abs(n-493.88)<=1:
    print("B")
else :
    print('Khong tim thay')
