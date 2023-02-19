k = int(input())
for i in range(k):
    a = [int(x) for x in input().split(' ')[:-1]]
    f = True
    ind = -1
    for i in range(1, len(a)-1):
        if a[i] > a[i-1] and a[i] > a[i+1] or a[i] < a[i-1] and a[i] < a[i+1]:
            continue
        f = False
        ind = i
        break
    if f:
        print(len(a))
    else:
        print(a[ind])
