a, b, c = map(int, input().split())
canhmax = max(a, b, c)
if a!=0 and b!=0 and c!=0:
    if a+b+c-canhmax > canhmax:
        print('Day la 3 canh cua mot tam giac')
        chuvi = float (a+b+c)
        nuachuvi = chuvi/2
        dientich = ((nuachuvi * (nuachuvi-a) * (nuachuvi-b) * (nuachuvi-c)) ** 0.5)
        print(f"{chuvi:.2f} {dientich:.1f}")
    else:
       print('Day khong phai la 3 canh cua mot tam giac')