#
#
# if __name__ == '__main__':
#     N = int(input())
#     for i in range(N):
#         c = input().split()
#         l = []
#         if c[0] == 'insert':
#             l.insert(int(c[1]), int(c[2]))
#             print(l)
#         elif c[0] == 'append':
#             l.append(int(c[1]))
#         elif c[0] == 'sort':
#             sorted(l)
#         elif c[0] == 'reverse':
#             l.reverse()
#         elif c[0] == 'remove':
#             l.remove(int(c[1]))
#         elif c[0] == 'pop':
#             l.pop()
#         elif c[0] == 'print':
#             print(l)
#
#


# Ninja Method to tackle List Operations

n=int(input())
l=[]
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != 'print':
        cmd += "(" + ",".join(args) + ")"
        eval("l."+cmd)
    else:
        print(l)