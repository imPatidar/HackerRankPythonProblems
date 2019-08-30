a = int(input())

for i in range(2 * a - 1):
    for j in range(2 * a - 1):
        print(1 + max(abs(a - i - 1), abs(a - j - 1)),end=" ")
    print()
