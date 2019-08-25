import itertools

t = set(itertools.permutations([int(x) for x in "5 1 2 4 4 2 4 2 2 5 1 4 3 1 1 1 2 1 4 1".split(" ")], 6))

c = 0
print(len(t))
a = []
for i in t:
    a.append(list(i))
for i in a:
    i.sort()


k = set(a)
print(len(k))
