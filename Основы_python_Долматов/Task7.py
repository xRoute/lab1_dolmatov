def pyramid(n):
    if n<=0:
        return "It is impossible"

    result = 0
    k = 0
    while result < n:
        k += 1
        result += k**2
    if result == n:
        return k
    else:
        return "It is impossible"