n = int(input())
f = True
while n > 0:
    a = int(input())
    if n - a >= 0 and (a == 1 or a == 3 or a == n / 2):
        n -= a
        f = not f
        print(n)
    else:
        print('Ошибка! Повторите ход')
if f:
    print('ИИ победил')
else:
    print('Света победила')
