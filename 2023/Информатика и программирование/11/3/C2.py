n = int(input())
a = [int(x) for x in input().split(' ')]
r = int(input())
min_abs = abs(a[0] - r)
min_a = a[0]
for i in range(1, n):
    if abs(a[i] - r) < min_abs:
        min_abs = abs(a[i] - r)
        min_a = a[i]
print(min_a)
