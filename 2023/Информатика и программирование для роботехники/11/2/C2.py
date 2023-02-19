a = '0123456789ABCDEF'
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                n = 'F' + x1 + x2 + x3 + x4 + 'A'
                if n.count('3B') == 1:
                    print(int(n, 16))
