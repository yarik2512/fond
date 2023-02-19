n, U, D, I, J, l = [int(x) for x in input().split(' ')]
edges = []
for i in range(n - 1):
    edges.append([i, i+1, U])
    edges.append([i+1, i, D])
for i in range(l):
    s = [int(x) for x in input().split(' ')]
    for i in range(1, s[0] + 1):
        for j in range(i + 1, s[0] + 1):
            edges.append([s[i]-1, s[j]-1, I + J])
            edges.append([s[j]-1, s[i]-1, I + J])
INF = 10 ** 10
distance = [INF for i in range(n)]
distance[0] = 0
for i in range(n):
    for e in edges:
        a, b, w = e
        distance[b] = min(distance[b], distance[a]+w)
print(distance[-1])
