from random import choice

def f():
    a = ['“орёл”- “орёл”', '“орёл-решка”', '“решка-орёл”', '“решка-решка”']
    cnt = [0, 0, 0, 0]
    for i in range(1000):
        c = choice([0, 1, 2, 3])
        cnt[c] += 1
    m = 0
    ind = 0
    for i in range(4):
        if cnt[i] > m:
            ind = i
            m = cnt[i]
    return a[ind]

print(f())
