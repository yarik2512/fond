gl = 'aeiouёуеыаоэяию'

def c(s):
    return sum([1 if x in gl else 0 for x in s])

n = int(input())
s = input()
prev = len(s) - c(s)
cnt = 0
for i in range(n-1):
    s = input()
    if c(s) == prev:
        cnt += 1
    prev = len(s) - c(s)
print(cnt)
