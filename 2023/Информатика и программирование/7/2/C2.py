a, b, c = [int(input()) for i in range(3)]
p = 1/2 * (a + b + c)
s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
print(s)
