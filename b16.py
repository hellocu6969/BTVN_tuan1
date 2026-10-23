a, b = map(float, input().split())
DTB = (a+b*2)/3
print(round(DTB,1))
if DTB >= 8:
    print("Gioi")
elif DTB >= 6.5:
    print("Kha")
elif DTB >= 5:
    print("Trung binh")
elif DTB >= 3.5:
    print("Yeu")
else:
    print("Kem")