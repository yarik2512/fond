k = int(input())
cnt = 0
for i in range(k):
    a = [int(x) for x in input().split(' ')[:-1]]
    f = True
    for i in range(1, len(a)-1):
        if a[i] > a[i-1] and a[i] > a[i+1] or a[i] < a[i-1] and a[i] < a[i+1]:
            continue
        f = False
        break
    if f:
        cnt += 1
print(cnt)
