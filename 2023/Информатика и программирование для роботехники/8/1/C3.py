m, n = [int(x) for x in input().split(' ')]
a = []
for i in range(m):
    a.append([int(x) for x in input().split(' ')])
for i in range(m):
    for j in range(n // 2):
        a[i][j], a[i][j+n//2] = a[i][j+n//2], a[i][j]
for i in range(m):
    print(' '.join(str(x) for x in a[i]))
