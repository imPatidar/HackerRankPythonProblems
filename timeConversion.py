import os
import sys

def timeConversion(s):
    # Write your code here.
    hr = s[0:2]
    if s[-2:] == 'PM':
        a = int(hr)
        a = a + 12
        t = str(a) + s[2:8]
    return t


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
