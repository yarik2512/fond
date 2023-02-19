cf = [i for i in range(10)]
s = 0
for a in cf:
    for b in cf:
        if b % 2 != 0:
            continue
        for c in cf:
            for d in cf:
                n = a * 1000 + b * 100 + c * 10 + d
                if n % 6 == 0 and n % 12 != 0:
                    s += n
print(str(s)[:4])
