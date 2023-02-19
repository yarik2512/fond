def is_palindrom(k):
    return str(k) == ''.join(reversed(str(k)))

k = int(input())
print(is_palindrom(k))
