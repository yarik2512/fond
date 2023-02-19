d = {
    'North': [0, 1],
    'South': [0, -1],
    'East': [1, 0],
    'West': [-1, 0]
}
i = input().split(' ')
if len(i) > 1:
    s, n = i
    n = int(n)  
else:
    s = i[0]
x, y = 0, 0
while s != 'Treasure!':
    x += n * d[s][0]
    y += n * d[s][1]
    i = input().split(' ')
    if len(i) > 1:
        s, n = i
        n = int(n)  
    else:
        s = i[0]
print(x, y)
