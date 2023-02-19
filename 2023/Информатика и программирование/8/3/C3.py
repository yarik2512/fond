s = 1000
p = int(input()) / 100
k = 0
while s <= 2000:
    s += s * p
    k += 1
print(k, s)
