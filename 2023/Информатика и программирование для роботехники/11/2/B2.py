a = [
    [1, 6],
    [2, 7],
    [3],
    [4, 6, 7],
    [0, 5, 6, 9],
    [0, 8],
    [7],
    [0, 2],
    [0],
    [5]
]

def f(a, v, i, j):
    if i == j:
        return 1
    r = 0
    v[i] = True
    for x in a[i]:
        if v[x] == False:
            v[x] = True
            r += f(a, v, x, j)
            v[x] = False
    return r

def ans(a, i):
    r = 0
    for x in a[i]:
        r += f(a, [False for i in range(10)], x, i)
    return r

print(ans(a, 7))
