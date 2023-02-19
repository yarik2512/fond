r = int(input())
a = [int(x) for x in input()[:-2].split(' ')]
c = 0
n = 0
for x in a:
    if x > r:
        c += 1
        n = x
if c == 0:
    print(c, -1)
else:
    print(c, n)
