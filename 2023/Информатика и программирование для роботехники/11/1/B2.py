a = [
    [],
    [0],
    [0, 1, 3],
    [0, 4],
    [0],
    [1, 2],
    [2, 3, 4, 5, 7],
    [4],
    [5, 6, 7],
    [8],
    [8],
    [9, 10]
]

def f(a, i, j, k):
    if i == j:
        return 1
    r = 0
    for x in a[i]:
        if x == k:
            continue
        r += f(a, x, j, k)
    return r

print(f(a, 11, 0, 6))
