n = int(input())
a = [int(x) for x in input().split(' ')]
r = int(input())
min_abs = abs(a[0] + a[1] - r)
min_a0, min_a1 = a[0], a[1]
for i in range(1, n):
    if abs(a[i] + a[i+1] - r) < min_abs:
        min_abs = abs(a[i] + a[i+1] - r)
        min_a0 = a[i]
        min_a1 = a[i+1]
print(min(min_a0, min_a1), max(min_a0, min_a1))
