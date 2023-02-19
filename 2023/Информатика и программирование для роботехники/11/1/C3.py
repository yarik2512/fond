def DEL(n, m):
    return n % m == 0
A = 1
for i in range(1, 10000):
    f = True
    for x in range(-10000, 10000):
        if not(DEL(21, i) and (not(DEL(x, 40) and DEL(x, 30)) or DEL(x, i))):
            f = False
            break
    if f:
        A = i
print(A)
