s = input()
k, m = [int(x) for x in input().split(' ')]
s1 = s[k-1:m]
s = s[:k-1] + ''.join(reversed(s1)) + s[m:]
print(s)
for i in range(len(s)):
    if (i + 1)  % k == 0:
        s = s[:i] + s1[m % (m - k)] + s[i+1: ]
print(s)
