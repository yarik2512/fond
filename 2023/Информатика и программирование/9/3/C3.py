s = input()
c = input()
k = (32 + ord(s[0]) - ord(c)) % 32
r = ''
for i in range(len(s)):
    c = s[i]
    f = c.islower()
    c = c.upper()
    c = chr(ord('А') + (32 + ord(c) - ord('А') - k) % 32)
    if f:
        c = c.lower()
    r += c
print(k, r)
