a, n = [int(input()) for i in range(2)]
s = 0
for i in range(n+1):
    s += (-1) ** i * a ** i
print(s)
