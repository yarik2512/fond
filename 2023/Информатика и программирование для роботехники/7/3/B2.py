from random import shuffle

def deg(l):
    s = 1
    n = len(l)
    for i in range(n):
        if l[i] < i:
            s *= (i - l[i] + 1) / n
        else:
            s *= (i + (n - l[i]) + 1) / n
    return s

n = [x for x in range(10)]
for i in range(20):
    shuffle(n)
print(deg(n))

