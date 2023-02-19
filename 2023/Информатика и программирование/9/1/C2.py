s = input()
a = ''
n = len(s)
for i in range(1, n, 2):
    a += s[i]
if n % 2 == 0:
    for i in range(n-2, -1, -2):
        a += s[i]
else:
    for i in range(n-1, -1, -2):
        a += s[i]
print(a)
