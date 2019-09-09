from collections import Counter as c

def sherlockAndAnagrams(s):
    counts = 0
    for i in range(len(s)):
        substrings = ["".join(sorted(s[idx:idx + i + 1])) for idx in range(0, len(s))]
        counts += sum([(v - 1) * v // 2 for _, v in c(substrings).items()])
    return counts

print(sherlockAndAnagrams('abba'))