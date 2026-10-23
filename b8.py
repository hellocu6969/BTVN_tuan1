a,b,c = map(int, input().split())
nuachuvi = float((a+b+c)/2)
dientich = float((nuachuvi*(nuachuvi-a)*(nuachuvi-b)*(nuachuvi-c))**0.5)
print(round(a*b*c/(4*dientich),3))