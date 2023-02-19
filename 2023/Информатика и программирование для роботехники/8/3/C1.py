n = int(input())
a = [int(x) for x in input().split(' ')]
r = dict()
for x in a:
    if not x in r:
        r[x] = 1
    else:
        r[x] += 1
for x, c in r.items():
    if c == 1:
        print(x)
