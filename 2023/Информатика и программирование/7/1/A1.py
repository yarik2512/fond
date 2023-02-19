seasons = {
    'зима': ['декабрь', 'январь', 'февраль'],
    'весна': ['март', 'апрель', 'май'],
    'лето': ['июнь', 'июль', 'август'],
    'осень': ['сентябрь', 'октябарь', 'ноябрь'],
}
gl = 'ёуеыаоэяию'
months = {
    'январь': 31, 
    'февраль': 28,
    'март': 31,
    'апрель': 30,
    'май': 31,
    'июнь': 30,
    'июль': 31,
    'август': 31,
    'сентябрь': 30,
    'октябарь': 31,
    'ноябрь': 30,
    'декабрь': 31,
}

def c(m):
    return sum([1 if x in gl else 0 for x in m]) % 2 == 0

while True:
    season, days, b = input().replace(' ', '').split(',')
    days = int(days)
    b = bool(b)
    answer = []
    for month in seasons[season]:
        if b and c(month) and months[month] >= days:
            answer.append(month)
        elif not b and not c(month) and months[month] >= days:
            answer.append(month)
    if len(answer) == 0:
        continue
    else:
        print(', '.join(answer))
        break
