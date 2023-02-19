a = [int(x) for x in input().split(' ')]
b = []
for i in range(len(a)):
    b.append(sum(a[i:]))
print(' '.join(str(x) for x in b))
