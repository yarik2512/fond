def rec(n):
    if n == 1:
        print(1, end=' ')
        return 1
    if n == 2:
        print(2, end=' ')
        return 2
    a_n = (rec(n-2) + 2 * rec(n-1)) / 3
    print(a_n, end=' ')
    return a_n

def cycle(n):
    if n == 1:
        print(1)
        return
    if n == 2:
        print(1, 2)
        return
    p = 1
    a = 2
    print(1, 2, end=' ')
    for i in range(2, n):
        p, a = a, (p + 2*a) / 3
        print(a, end=' ')

def dyn(n):
    d = []
    d.append(1)
    d.append(2)
    for i in range(2, n):
        d.append((d[-2] + 2 * d[-1]) / 3)
    for x in d:
        print(x, end=' ')
