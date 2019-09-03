import os


def utopianTree(n):
    c = 0
    for i in range(n + 1):

        if i % 2 == 0:
            c += 1
        else:
            c *= 2
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
