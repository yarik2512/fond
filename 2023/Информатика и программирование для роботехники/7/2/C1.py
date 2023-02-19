n = input()
n1 = n2 = 0
for x in n:
    if int(x) % 3 == 0:
        n1 += 1
    if int(x) % 2 != 0:
        n2 += 1
if n1 > n2:
    for i in range(0, len(n), 3):
        print(n[i], end='')
else:
    for i in range(0, len(n), 2):
        print(n[i], end='')
