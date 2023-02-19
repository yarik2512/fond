def rec(n):
    if n == 1:
        print(1, end=' ')
        return 1
    if n == 2:
        print(2, end=' ')
        return 2
    if n == 3:
        print(3, end=' ')
        return 3
    a_n = rec(n-1) + rec(n-2) - 2 * rec(n-3)
    print(a_n, end=' ')
    return a_n

def cycle(n):
    if n == 1:
        print(1)
        return
    if n == 2:
        print(1, 2)
        return
    if n == 3:
        print(1, 2, 3)
        return
    pp = 1
    p = 2
    a = 3
    print(1, 2, 3, end=' ')
    for i in range(3, n):
        pp, p, a = p, a, a + p - 2 * pp
        print(a, end=' ')

def dyn(n):
    d = []
    d.append(1)
    d.append(2)
    d.append(3)
    for i in range(3, n):
        d.append(d[-1] + d[-2] - 2 * d[-3])
    for x in d:
        print(x, end=' ')
