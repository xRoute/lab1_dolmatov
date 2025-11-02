def magic(n):
    count = 0
    while n>9:
        next_n = 1
        for a in str(n):
            next_n *= int(a)
        n = next_n
        count+=1
    return count