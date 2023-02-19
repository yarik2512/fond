a, b, c = [int(x) for x in input()]
m = 100 * (a + b + c)
if a != 0:
    m = min(m, a * 100 + min(b, c) * 10 + max(b, c))
if b != 0:
    m = min(m, b * 100 + min(a, c) * 10 + max(a, c))
if c != 0:
    m = min(m, c * 100 + min(a, b) * 10 + max(a, b))
print(m)
