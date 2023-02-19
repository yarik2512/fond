s = n = 0
max_x = 0
for x in range(4000, 11001):
    if (x % 5 == 0 or x % 23 == 0) and x % 7 != 0 and x % 10 != 0 and (x // 10 % 10 == 1 or x // 10 % 10 == 3):
        s += x
        n += 1
        max_x = x
print(s // n, max_x)
