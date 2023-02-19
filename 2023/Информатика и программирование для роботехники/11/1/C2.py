l = 'qwertyuiopasdfghjklzxcvbnm'
g = 'aeiouy'
cnt = 0
for l1 in l:
    for l2 in l:
        for l3 in l:
            for l4 in l:
                for l5 in l:
                    w = l1 + l2 + l3 + l4 + l5
                    if any([x in g for x in w]):
                        cnt += 1
print(cnt)
