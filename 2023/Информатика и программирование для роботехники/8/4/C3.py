n, m = [int(x) for x in input().split()]
a = [[0 for j in range(m)] for i in range(n)]
i = j = 0
c = 1
while True:
    if not(0 <= i < n and 0 <= j < m) or a[i][j] != 0:
        break
    while j < m and a[i][j] == 0:
        a[i][j] = c
        c += 1
        j += 1
    j -= 1
    i += 1
    if not(0 <= i < n and 0 <= j < m) or a[i][j] != 0:
        break
    while i < n and a[i][j] == 0:
        a[i][j] = c
        c += 1
        i += 1
    i -= 1
    j -= 1
    if not(0 <= i < n and 0 <= j < m) or a[i][j] != 0:
        break
    while j >= 0 and a[i][j] == 0:
        a[i][j] = c
        c += 1
        j -= 1
    j += 1
    i -= 1
    if not(0 <= i < n and 0 <= j < m) or a[i][j] != 0:
        break
    while i >= 0 and a[i][j] == 0:
        a[i][j] = c
        c += 1
        i -= 1
    i += 1
    j += 1
for i in range(n):
    print(' '.join(str(x) for x in a[i]))
