thang, nam = map(int, input().split())
if thang == 2:
    if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
        print("29")
    else:
        print("28")
elif thang in (1,3,5,7,8,10,12):
    print("31")
else:
    print("30")