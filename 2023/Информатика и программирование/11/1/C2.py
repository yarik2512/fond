n = int(input())
a = [int(x) for x in input().split(' ')]
r = int(input())
min_abs = abs(a[0] + a[1] - r)
min_a0, min_a1 = a[0], a[1]
for i in range(n):
    for j in range(i+1, n):
        if abs(a[i] + a[j] - r) < min_abs:
            min_abs = abs(a[i] + a[j] - r)
            min_a0 = a[i]
            min_a1 = a[j]
print(min_a0, min_a1)
