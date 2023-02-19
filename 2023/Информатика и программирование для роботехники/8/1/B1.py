def snowflake_recurtion(n):
    if n == 1:
        return 6
    return 5 * snowflake_recurtion(n-1)

def snowflake_cycle(n):
    r = 6
    for i in range(1, n):
        r *= 5
    return r
