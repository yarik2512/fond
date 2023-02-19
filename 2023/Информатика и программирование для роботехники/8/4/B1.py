def trib_rec(n):
    if n < 3:
        return 1
    return trib_rec(n-1) + trib_rec(n-2) + trib_rec(n-3)

def trib_cycle(n):
    r = 1
    p = 1
    pp = 1
    for i in range(2, n):
        pp, p, r = p, r, pp + p + r
    return r
