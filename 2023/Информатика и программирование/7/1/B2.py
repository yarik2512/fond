prev = len(input())
a = []
s = input()
while s != '':
    if len(s) > prev:
        a.append(s)
    prev = len(s)
    s = input()
for x in reversed(a):
    print(x)
