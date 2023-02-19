A = 1000
for i in range(1000, -1000, -1):
    f = True
    for x in range(-100, 100):
        for y in range(-100, 100):
            if not((x - 20 < i) and (20 - x < i) or (x * y > 5)):
                f = False
                break
    if f:
        A = i
print(A)
