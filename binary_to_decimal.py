def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n / 2))


def binary_to_decimal(n1):
    n = len(n1)
    res = 0
    for i in range(1, n + 1):
        res = res + int(n1[i - 1]) * 2 ** (n - i)
    return res


# print(decimal_to_binary(4))
print(binary_to_decimal('10000'))
