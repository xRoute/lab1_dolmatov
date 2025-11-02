def check_individual_letter(line):
    letters=[]
    for i in line.lower():
        if i in letters:
            return False
        else:
            letters.append(i)
    return True
