def subsets(s):
    if not s:
        return [s]
    sets = [s]
    for i in range(0, len(s)):
        tmp_subsets = subsets(s[:i] + s[i + 1:])
        for subset in tmp_subsets:
            if subset not in sets:
                sets.append(subset)
    return sets


s = [g for g in range(10)]
k = subsets(s)
for x in k:
    if len(x) == 2:
        print(x, end=" ")
