def pif_rec(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return pif_rec(n-1) + (pif_rec(n-1) - pif_rec(n-2)) * 2

def pif_cycle(n):
    r = 1
    p = 0
    for i in range(n):
        r, p = r + (r - p) * 2, r
    return r
