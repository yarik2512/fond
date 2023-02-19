n, m = [int(x) for x in input().split(' ')]
d = [0 for i in range(n)]
for i in range(m):
    x, y = [int(x) for x in input().split(' ')]
    d[x-1] += 1
    d[y-1] += 1
for i in range(1, n):
    if d[i] != d[i-1]:
        print('NO')
        exit()
print('YES')
