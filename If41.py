# 41
note=input("not nhac:")
h=note[0]
g=int(note[1:3])
if h=='A' or h=='B' or h=='C' or h=='D' or h=='E' or h=='F' or h=='G' :
    if g<0 or g>8 :
        print('Khong hop le')
    elif h=='A':
        f=440.00/(2**(4-g))
        print(f)
    elif h=='B':
        f=493.88/(2**(4-g))
        print(f)
    elif h=='C':
        f=261.63/(2**(4-g))
        print(f)
    elif h=='D':
        f=293.66/(2**(4-g))
        print(f)
    elif h=='E':
        f=329.63/(2**(4-g))
        print(f)
    elif h=='G':
        f=392.00/(2**(4-g))
        print(f)
    elif h=='F':
        f=349.23/(2**(4-g))
        print(f)
else :
    print('Khong hop le')   
