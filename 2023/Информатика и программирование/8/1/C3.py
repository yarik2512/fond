A, B, C = [int(input()) for i in range(3)]
x = y = 0
for i in range(0, A, C):
    x += 1
for i in range(0, B, C):
    y += 1
print(x * y)
