bienso = str(input())
a = int(bienso[0])
b = int(bienso[1])
c = int(bienso[2])
d = int(bienso[3])
e = int(bienso[4])
kq = (a+b+c+d+e) % 10
if kq == 9:
    print ("9")
    print ('may man')
else:
    print (kq)
    print ('khong may man')