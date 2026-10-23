tien = int (input())
tien = tien / 1000
nam = int(tien // 5)
tien = tien % 5
hai = int(tien // 2)
tien = tien % 2
mot = int(tien // 1)
print (nam, hai, mot)