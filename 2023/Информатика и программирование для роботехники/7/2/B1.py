n = int(input())
d = dict()
for i in range(n):
    a, b = input().split(' ')
    d[a] = b
    d[b] = a
s = input().split(' ')
for x in s:
    if x in d:
        print(d[x], end=' ')
