def number_expansion(n):
    i = 2
    numbers = {}
    while i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            numbers[i] = count
        i += 1
    if n > 1:
        numbers[n] = 1

    result = ""
    for prime, power in numbers.items():
        if power == 1:
            result += f"({prime})"
        else:
            result += f"({prime}**{power})"
    return result