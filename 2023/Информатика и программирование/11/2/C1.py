f = open('Пушкин Александр. Капитанская дочка.ru', 'r')
max_sent = 0
sent = ''
for line in f:
    s = line.replace(' ', '')
    s = s.replace('!', '.')
    s = s.replace('?', '.')
    s = s.replace('...', '.')
    for x in s.split('.'):
        if len(x) > max_sent:
            max_sent = len(x)
            sent = x
