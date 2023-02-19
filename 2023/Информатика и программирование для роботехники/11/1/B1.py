n = int(input())
d = []
for i in range(n):
    d.append(0)
    for x in input().split(' '):
        if int(x):
            d[-1] += 1
for x in d:
    print(x)
