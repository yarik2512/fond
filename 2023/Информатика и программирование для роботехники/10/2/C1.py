n = int(input())
s = 0
for i in range(1, n+1):
    p = 1
    for j in range(i):
        p *= i
    s += p
print(s)
