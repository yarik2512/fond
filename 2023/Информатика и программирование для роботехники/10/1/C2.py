m, n = [int(x) for x in input().split(' ')]
a = [[] for x in range(n)]
for i in range(m):
    col = [int(x) for x in input().split(' ')]
    for j in range(n):
        a[j].append(col[j])
for i in range(n-1):
    for j in range(n-1-i):
        if max(a[j]) > max(a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
for i in range(m):
    for j in range(n):
        print(a[j][i], end=' ')
    print()
