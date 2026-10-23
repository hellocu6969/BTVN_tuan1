a, b, c = map(int, input().split())
if a == b & b == c:
    print("=")
else:
    max = max(a, b, c)
    print(max)