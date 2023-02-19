m = int(input())
a = []
for i in range(m):
    a.append([int(x) for x in input().split(' ')])
for i in range(m):
    for j in range(m // 2):
        a[i][j], a[i][m-j-1] = a[i][m-j-1], a[i][j]
for i in range(m // 2):
    for j in range(m):
        a[i][j], a[m-i-1][j] = a[m-i-1][j], a[i][j]
for i in range(m):
    print(' '.join(str(x) for x in a[i]))
