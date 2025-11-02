def is_balanced(n):
    numbers = [int(i) for i in str(n)]
    k = len(numbers)

    if k % 2 == 0:
        mid_left = k//2 - 1
        mid_right = k//2
        left = numbers[:mid_left]
        right = numbers[mid_right+1:]
    else:
        mid = k//2
        left = numbers[:mid]
        right = numbers[mid+1:]

    return sum(left) == sum(right)