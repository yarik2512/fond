from statistics import median

a, b, c = [int(input()) for i in range(3)]
arf = (a + b + c) / 3
if arf > median([a, b, c]):
    print(arf)
else:
    print(0)
