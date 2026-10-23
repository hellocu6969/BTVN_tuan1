km = int(input())
if km <= 1:
    print("12000")
elif km <= 30:
    print(12000 + (km - 1) * 10000)
else:
    print(12000 + 29 * 10000 + (km - 30) * 9000)