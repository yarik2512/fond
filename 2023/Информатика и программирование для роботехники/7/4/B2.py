from random import random

def f():
    a = [random() for i in range(10)]
    s1 = sum(a) // 1
    a.extend([random() for i in range(10)])
    s2 = sum(a) // 1
    return s1, s2

print(f())
