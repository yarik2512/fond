a = '.,;:…!?-()"'

def c(s):
    return sum([1 if x in a else 0 for x in s])

s = input()
prev = c(s)
r = []
while s != '':
    s = input()
    if c(s) > prev:
        r.append(s)
    prev = c(s)
for x in reversed(r):
    print(x)
