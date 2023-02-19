m = int(input())
a = []
for i in range(m):
    a.append([int(x) for x in input().split(' ')])
for j in range(m):
    for i in range(m - j):
        a[i][j], a[m-j-1][m-i-1] = a[m-1-j][m-1-i], a[i][j]
for i in range(m // 2):
    for j in range(m):
        a[i][j], a[m-i-1][j] = a[m-i-1][j], a[i][j]
for j in range(m):
    for i in range(m - j):
        a[i][j], a[m-j-1][m-i-1] = a[m-1-j][m-1-i], a[i][j]
for i in range(m // 2):
    for j in range(m):
        a[i][j], a[m-i-1][j] = a[m-i-1][j], a[i][j]
for j in range(m):
    for i in range(m - j):
        a[i][j], a[m-j-1][m-i-1] = a[m-1-j][m-1-i], a[i][j]
for i in range(m // 2):
    for j in range(m):
        a[i][j], a[m-i-1][j] = a[m-i-1][j], a[i][j]
for i in range(m):
    print(' '.join(str(x) for x in a[i]))
