n = int(input())
cnt = 0
for x in range(10 ** (n - 1), 10 ** n):
    if (x % 2 == 0 or x % 3 == 0) and x % 6 != 0:
        cnt += 1
print(cnt)
