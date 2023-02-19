from random import randrange, randint

def choose_rand_seq(n):
    if n == 2:
        a, b = [int(input()) for i in range(n)]
        return randint(a, b)
    if n == 3:
        a, b, c = [int(input()) for i in range(n)]
        return randrange(a, b, c)

print(randrange.__doc__)
print(randint.__doc__)
