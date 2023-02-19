n = int(input())
a = [[1 if (i + j) % 2 == 0 else 0 for j in range(n)] for i in range(n)]
for i in range(n):
    print(' '.join(str(x) for x in a[i]))
