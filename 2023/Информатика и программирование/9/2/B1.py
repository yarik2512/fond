s = input().split(' ')
c = []
for x in s:
    if x == '+':
        t = c.pop()
        c[-1] += t
    elif x == '-':
        t = c.pop()
        c[-1] -= t
    elif x == '*':
        t = c.pop()
        c[-1] *= t
    else:
        c.append(int(x))
print(c.pop())
