n = int(input())
s = 0
for i in range(n):
    s += (-1) ** i * (1.1 + i * 0.1)
print(s)
