import datetime


def pow_fast(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return pow_fast(a, b // 2) * pow_fast(a, b // 2)
    else:
        return pow_fast(a, (b - 1) // 2) * pow_fast(a, (b - 1) // 2) * a


before = datetime.datetime.now()
print(len(str(pow_fast(23, 200))))
print(datetime.datetime.now() - before)
