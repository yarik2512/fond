s = 10
p = int(input())
d = 1
while s <= 200:
    s += s * p / 100
    d += 1
print(d, s)
