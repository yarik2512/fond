s = input()
n = len(s)
a1 = a2 = ''
for i in range(n - 1, n // 2 - 1, -1):
    a1 += s[i]
for i in range(n // 2):
    a2 += s[i]
a = ''
if len(a1) == len(a2):
    for i in range(len(a1)):
        a += a1[i] + a2[i]
else:
    a += a1[0]
    for i in range(len(a2)):
        a += a2[i] + a1[1 + i]
print(a)
