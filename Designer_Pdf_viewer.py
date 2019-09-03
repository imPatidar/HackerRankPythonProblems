
a = [int(i) for i in input().split()]
wordDiff = [a[ord(c)-ord('a')] for c in input()]
print(max(wordDiff)*len(wordDiff))