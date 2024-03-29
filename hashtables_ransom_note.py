from collections import Counter


def checkMagazine(magazine, note):
    return (Counter(note) - Counter(magazine)) == {}


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print("Yes" if checkMagazine(magazine, note) else "No")
