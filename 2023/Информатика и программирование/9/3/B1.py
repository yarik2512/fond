def cmp(a, b):
    if a == 0 and b == 0:
        return 1
    if a == 9 and b == 0:
        return 0
    return a > b

first = list(map(int, input().split(' ')))
second = list(map(int, input().split(' ')))
cnt = 0
while len(first) > 0 and len(second) > 0 and cnt < 107:
    if cmp(first[0], second[0]):
        first.append(first[0])
        first.append(second[0])
    else:
        second.append(first[0])
        second.append(second[0])
    first.pop(0)
    second.pop(0)
    cnt += 1
if len(first) == 0:
    print('second', cnt)
elif len(second) == 0:
    print('first', cnt)
else:
    print('botva')
