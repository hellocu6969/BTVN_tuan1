giay = int(input())
gio = giay // 3600
giay = giay - (gio * 3600)
phut = giay // 60
giay = giay - (phut * 60)
print(gio,":", phut,":", giay, sep="")