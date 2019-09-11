def count_substring(s1, s2):
    c = 0
    for i in range(len(s1)):
        if s1[i:].startswith(s2):
            c += 1
    return c
