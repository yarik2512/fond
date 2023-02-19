s = input()
k = int(input())
r = ''
for i in range(len(s)):
    c = s[i]
    f = c.islower()
    c = c.upper()
    c = chr(ord('А') + (ord(c) - ord('А') + k) % 32)
    if f:
        c = c.lower()
    r += c
print(r)
