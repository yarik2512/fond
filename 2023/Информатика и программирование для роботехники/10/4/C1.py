k = int(input())
for i in range(k):
    a = [int(x) for x in input().split(' ')[:-1]]
    b = [1 if a[i+1] > a[i] else 0 if a[i+1] == a[i] else -1 for i in range(len(a)-1)]
    if min(b) == 0:
        print(max(b))
    elif max(b) == 0:
        print(min(b))
    elif min(b) == max(b):
        print(max(b))
    else:
        print(0)

