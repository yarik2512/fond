def rec(n):
    if n == 1:
        print(1.0, end=' ')
        return 1
    a_n = (rec(n-1) + 1) / n
    print(a_n, end=' ')
    return a_n

def cycle(n):
    a = 0
    for i in range(1, n+1):
        a = (a + 1) / i
        print(a, end=' ')

def dyn(n):
    d = []
    d.append(1.0)
    for i in range(2, n+1):
        d.append((d[-1] + 1) / i)
    for x in d:
        print(x, end=' ')
