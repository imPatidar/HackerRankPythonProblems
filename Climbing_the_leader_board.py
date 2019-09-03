scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
board = sorted(set(scores), reverse=True)
c = len(board)

for a in alice:
    while (c > 0) and (a >= board[c - 1]):
        c -= 1
    print(c + 1)
