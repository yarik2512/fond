s = input().split(' ')
k, m = [int(x) for x in input().split(' ')]
c = 0
while len(s) < k:
    s.append(s[c])
    c += 1
a = []
for i in range(k-1, len(s), k):
    a.append(s[i])
for i in range(len(a)):
    if len(a[i]) < m:
        a.pop(i)
for x in a:
    print(x)
