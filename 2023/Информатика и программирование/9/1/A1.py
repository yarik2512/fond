n = int(input())
p = [int(x) for x in input().split(' ')]
m = int(input())
edges = []
for i in range(m):
    x, y = [int(x) for x in input().split(' ')]
    edges.append([x-1, y-1, p[x-1]])
    edges.append([y-1, x-1, p[y-1]])
distance = [1000000000 for i in range(n)]
distance[0] = 0
for i in range(n):
    for e in edges:
        a, b, w = e
        distance[b] = min(distance[b], distance[a]+w)
print(distance[n-1] if distance[n-1] != 1000000000 else -1)
