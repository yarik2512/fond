f = open('Пушкин Александр. Капитанская дочка.ru', 'r')
max_len = 0
word = ''
d = dict()
for line in f:
    s = line.replace('.', '')
    s = line.replace('?', '')
    s = line.replace('!', '')
    s = line.replace(';', '')
    s = line.replace(':', '')
    s = line.replace(',', '')
    words = s.split(' ')
    for w in words:
        if not w in d:
            d[w] = 0
        else:
            d[w] += 1
        if len(w) > max_len:
            max_len = len(w)
            word = w
print(word, max(d, key=d.get))

