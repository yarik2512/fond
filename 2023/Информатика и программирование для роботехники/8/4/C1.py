a = [int(x) for x in input().split()[:-1]]
n = len(a)
c = 0
for i in range(n):
    f = 1
    for j in range(i+1, n):
        if a[i] >= a[j]:
            f = 0
            break
    if f:
        print(a[i], end=' ')
        c += 1
print()
print(n, c)
