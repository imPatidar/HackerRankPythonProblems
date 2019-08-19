def gcd(a,b):
    while a%b != 0:
        a,b = b, ( a % b )
    return b

print(gcd(4,12))