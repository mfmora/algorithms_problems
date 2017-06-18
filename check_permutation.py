def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    letters = {}

    for i in range(0,len(string1)):
        letters.setdefault(string1[i],0)
        letters.setdefault(string2[i],0)
        letters[string1[i]] += 1
        letters[string2[i]] -= 1

    return all(value == 0 for value in letters.itervalues())
