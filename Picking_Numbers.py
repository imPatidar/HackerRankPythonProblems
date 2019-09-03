import os
from collections import defaultdict

def pickingNumbers(a):
    d = defaultdict(int)
    r = 0
    for val in a:
        d[val] += 1
        r = max(r, d[val] + d[val + 1], d[val] + d[val - 1])
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
