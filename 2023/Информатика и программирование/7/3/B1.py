cnt = 0
for x in range(100, 1000):
    if x // 100 != 0 and x % (x // 100) == 0 and x // 10 % 10 != 0 and x % (x // 10 % 10) == 0 and x % 10 != 0 and x % (x % 10) == 0:
        cnt += 1
print(cnt)
