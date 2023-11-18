#69
t=3
for i in range (1,16):
    x=(-1)**(i+1)
    y=(2*i*(2*i+1)*(2*i+2))
    t+=x*(4/y)
    print("n=",i,":",t)