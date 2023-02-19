m = int(input())
a = []
for i in range(m):
    a.append([int(x) for x in input().split(' ')])
for i in range(m):
    for j in range(m-i-1):
        a[i][j], a[m-j-1][m-i-1] = a[m-j-1][m-i-1], a[i][j]
for i in range(m):
    print(' '.join(str(x) for x in a[i]))
