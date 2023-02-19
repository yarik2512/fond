def power_3(a, b, c, d):
    return a ** b, a ** c, a ** d

a, b, c, d = [int(input()) for i in range(4)]
for x in power_3(a, b, c, d):
    print(x)
