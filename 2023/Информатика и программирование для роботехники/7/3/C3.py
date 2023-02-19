s = n = 0
min_x = 0
for x in range(4700, 9001):
    if x % 5 == 0 and x % 17 == 0 and x % 7 != 0 and x % 14 != 0 and (x // 10 % 10 >= x // 100 % 10):
        s += x
        n += 1
        if min_x == 0:
            min_x = x
print(s)
