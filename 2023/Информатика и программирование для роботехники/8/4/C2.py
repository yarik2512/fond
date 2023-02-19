a = [int(x) for x in input().split(' ')]
b = []
n = len(a)
for i in range(n):
    b.append(sum(a[i:]) / (n-i))
print(' '.join(str(x) for x in b))
