n = input()
n1 = n2 = 0
for x in n:
    if int(x) > 5:
        n1 += 1
    else:
        n2 += 1
if n1 > n2:
    print(''.join(reversed(n)))
else:
    for i in range(1, n1+n2, 2):
        print(n[i], end='')
