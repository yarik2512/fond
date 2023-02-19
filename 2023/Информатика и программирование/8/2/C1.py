def addNewDigit(a, r, d):
    if r == 'right':
        return int(str(a) + str(d))
    if r == 'left':
        return int(str(d) + str(a))

a, r, d = int(input()), input(), int(input())
print(addNewDigit(a, r, d))
