s = 0
n = 0
max_a = 0
for x in range(2300, 15001):
    if (x % 6 == 0 or x % 11 == 0) and x % 5 != 0 and x % 7 != 0 and (x // 100) % 10 != (x // 10) % 10:
        s += x
        n += 1
        max_a = x
print(s // n, max_a)
