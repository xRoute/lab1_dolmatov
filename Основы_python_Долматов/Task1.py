def count_vowels(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in line.lower():
        if i in vowels:
            count+=1
    return count

