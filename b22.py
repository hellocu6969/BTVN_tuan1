dien = int(input())
if dien <= 50:
    print(dien * 600)
elif dien <= 100:
    print(50 * 600 + (dien - 50) * 800)
elif dien <= 200:
    print(50 * 600 + 50 * 800 + (dien - 100) * 1100)
else:
    print(50 * 600 + 50 * 800 + 100 * 1100 + (dien - 200) * 1500)
