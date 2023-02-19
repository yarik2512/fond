n = int(input())
d = dict()
for i in range(n):
    ru, en = input().split(' ')
    d[ru] = en
s = input().split(' ')
for i in range(len(s)):
    s[i] = d[s[i]]
print(' '.join(s))
