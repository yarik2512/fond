N, K = [int(input()) for i in range(2)]
s = 0
for i in range(1, N+1):
    t = 1
    for j in range(K):
        t *= i
    s += t
print(s)
