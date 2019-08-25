# if __name__ == '__main__':
#     l = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         # l.append(name)
#         # m.append(score)
#         m = []
#         m.append(score)
#         m.append(name)
#         l.append(m)
#
#     t = sorted(l, key=lambda i: (i[1], i[0]), reverse=True)[-2][0]
#     # print(t)
#     q = []
#     for i in l:
#         if i[0] == t:
#             q.append(i[1])
#     print('\n'.join(sorted(q)))
#
#     # t=sorted(m)[-3]
#     # for i in l:
#
#
#

# Optimized Code

if __name__ == '__main__':
    n=int(input())
    marksheet=[[input(),float(input())] for _ in range(n)]
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))




