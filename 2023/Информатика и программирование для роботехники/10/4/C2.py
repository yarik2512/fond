m, n = [int(x) for x in input().split(' ')]
a = []
for i in range(m):
    a.append([int(x) for x in input().split(' ')])
for i in range(m-1):
    for j in range(m-1-i):
        if a[j][0] > a[j+1][0]:
            a[j], a[j+1] = a[j+1], a[j]
for i in range(m):
    print(' '.join(str(x) for x in a[i]))
