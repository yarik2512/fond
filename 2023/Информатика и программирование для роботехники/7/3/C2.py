s = input().split(' ')
k, m = [int(x) for x in input().split(' ')]
for i in range(len(s)):
    if len(s[i]) < k:
        s[i] = s[i] + '#'
    else:
        if len(s) < m:
            s[i] = s[i][:k-1] + '!' + s[i][k:]
        else:
            s[i] = s[i][:k-1] + s[i][m-1] + s[i][k:]
    print(s[i], end=' ')
