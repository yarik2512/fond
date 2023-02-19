s = input().split(' ')
k, m = [int(x) for x in input().split(' ')]
if len(s) < k:
    print(f'{k}-го слова нет в строке {" ".join(s)}')
else:
    x = s[k-1][m-1:]
    if len(x) == 0:
        print(''.join(reversed(s[k-1])))
    else:
        print(x)
