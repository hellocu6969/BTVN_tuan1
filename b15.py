a, b, c = map(int, input().split())
canhmax = max(a, b, c)
if a+b+c-canhmax > canhmax:
    print('Day la 3 canh cua 1 tam giac')
    chuvi = float (a+b+c)
    nuachuvi = chuvi/2
    dientich = ((nuachuvi * (nuachuvi-a) * (nuachuvi-b) * (nuachuvi-c)) ** 0.5)
    print(round(chuvi, 2), round(dientich, 1))
else:
    print('Day khong phai la 3 canh cua 1 tam giac')