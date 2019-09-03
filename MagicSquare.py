p = [[int(i) for i in input().split(" ")] for j in range(3)]
s = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2], [2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8],
     [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [4, 9, 2, 3, 5, 7, 8, 1, 6]]
# Print the minimum cost of converting 's' into a magic square
r = []
for i in range(8):
    r.append(0)
    for j in range(9):
        r[i] += abs(s[i][j] - p[int(j // 3)][j % 3])
print(min(r))

# Another Solution

seed = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
seeds = [seed, [list(t) for t in list(zip(*seed))]]
# transpose

squares = []

for square in seeds:
    squares.append(square)
    # mirror top down
    squares.append(square[::-1])
    # mirror left right
    squares.append([l[::-1] for l in square])
    # mirror + mirror(transpose + transpose)
    squares.append([l[::-1] for l in reversed(square)])

s = []
for s_i in range(3):
    s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
    s.append(s_t)
    #  Print the minimum cost of converting 's' into a magic square

minimum = min(sum(sum(abs(c1 - c2) for c1, c2 in zip(r1, r2)) for r1, r2 in zip(square, s)) for square in squares)

print(minimum)
