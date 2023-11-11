# 39
n=int(input('Muc decibel:'))
if n<40 :
    print('Âm thanh bé hơn Căn phòng im lặng')
elif n==40:
    print('Căn phòng im lặng')
elif 40<n<70 :
    print('Giữa Căn phòng im lặng và Đồng hồ báo thức')
elif n==70 :
    print('Đồng hồ báo thức')
elif 70<n<106 :
    print('Giữa Đồng hồ báo thức và Máy căn cỏ dùng gas')
elif n==106 :
    print('Máy cắt cỏ dùng gas')
elif 106<n<130 :
    print('Giữa Máy cắt cỏ dùng gas và búa khoan')
elif n==130 :
    print('búa khoan')
else :
    print('Âm thanh lớn hơn búa khoan')
