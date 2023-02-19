a = {
    '{': -1,
    '}': 1,
    '[': -2,
    ']': 2,
    '(': -3,
    ')': 3,
}
s = []
c = input()
for x in c:
    t = a[x]
    if t < 0:
        s.append(t)
    else:
        if len(s) == 0 or t + s.pop() != 0:
            print('no')
            exit()
if len(s) == 0:
    print('yes')
else:
    print('no')
