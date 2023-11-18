#70
n=input("Nhap tin nhan:")
mh=''
for i in n:
    if i=='A' or i=='a':
        mh+='D'
    elif i=='B' or i=='b':
        mh+='E'
    elif i=='C' or i=='c':
        mh+='F'
    elif i=='D' or i=='d':
        mh+='G'
    elif i=='E' or i=='e':
        mh+='H'
    elif i=='F' or i=='f':
        mh+='I'
    elif i=='G' or i=='g':
        mh+='J'
    elif i=='H' or i=='h':
        mh+='K'
    elif i=='I' or i=='i':
        mh+='L'
    elif i=='J' or i=='j':
        mh+='M'
    elif i=='K' or i=='k':
        mh+='N'
    elif i=='L' or i=='l':
        mh+='O'
    elif i=='M' or i=='m':
        mh+='P'
    elif i=='N' or i=='n':
        mh+='Q'
    elif i=='O' or i=='o':
        mh+='R'
    elif i=='P' or i=='p':
        mh+='S'
    elif i=='Q' or i=='q':
        mh+='T'
    elif i=='R' or i=='r':
        mh+='U'
    elif i=='S' or i=='s':
        mh+='V'
    elif i=='T' or i=='t':
        mh+='W'
    elif i=='U' or i=='u':
        mh+='X'
    elif i=='V' or i=='v':
        mh+='Y'
    elif i=='W' or i=='w':
        mh+='Z'
    elif i=='X' or i=='x':
        mh+='A'
    elif i=='Y' or i=='y':
        mh+='B'
    elif i=='Z' or i=='z':
        mh+='C'
    else:
        mh+=i
print(mh)