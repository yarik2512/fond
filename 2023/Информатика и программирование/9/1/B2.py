n, m = [int(x) for x in input().split(' ')]
a = [set() for x in range(n)]
for i in range(m):
    x, y = [int(x) for x in input().split(' ')]
    a[x-1].add(y-1)
    a[y-1].add(x-1)
for x in a:
    if len(x) != n - 1:
        print('NO')
        exit()
print('YES')
