n = input()
s1 = 0
s2 = 0
for i in range(5):
    s1 += int(n[i])
for i in range(5, 10):
    s2 += int(n[i])
s = 0
for i in range(1 if s1 > s2 else 0, 10, 2):
    s += int(n[i])
print(s)
