m, n = [int(x) for x in input().split(' ')]
a = []
for i in range(m):
    a.append([int(x) for x in input().split(' ')])
for j in range(n):
    max_x = a[0][j]
    max_i = 0
    min_x = a[0][j]
    min_i = 0
    for i in range(m):
        if a[i][j] < min_x:
            min_x = a[i][j]
            min_i = i
        if a[i][j] > max_x:
            max_x = a[i][j]
            max_i = i
    a[max_i], a[min_i] = a[min_i], a[max_i]
for i in range(m):
    print(' '.join([str(x) for x in a[i]]))
