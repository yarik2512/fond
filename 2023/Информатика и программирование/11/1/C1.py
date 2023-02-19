f = open('Пушкин Александр. Капитанская дочка.ru', 'r')
a = 'ёуеыаоэяию'
max_cnt = 0
word = ''
for line in f:
    s = line.replace('.', '')
    s = line.replace('?', '')
    s = line.replace('!', '')
    s = line.replace(';', '')
    s = line.replace(':', '')
    s = line.replace(',', '')
    words = s.split(' ')
    for w in words:
        cnt = 0
        for l in w:
            if l.lower() in a:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            word = w
print(word)
