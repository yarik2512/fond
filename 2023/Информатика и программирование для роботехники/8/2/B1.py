def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_cycle(n):
    p = 1
    r = 1
    for i in range(1, n):
        p, r = r, p+r
    return r
