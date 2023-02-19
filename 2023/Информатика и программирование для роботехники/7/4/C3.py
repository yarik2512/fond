s = n = 0
min_x = 0
max_x = 0
for x in range(4700, 9001):
    if x % 6 == 0 and x % 15 == 0 and x % 7 != 0 and x % 16 != 0 and ((x // 10 % 10 + x // 100 % 10) % 2 == 0):
        s += x
        n += 1
        max_x = x
        if min_x == 0:
            min_x = x
print(s)
