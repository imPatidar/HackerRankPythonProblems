def lrotate(a,d):
    mod=d%len(a)
    for i in range(len(a)):
        print(str(a[(mod+1)%len(a)]),end=" ")


nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
result = lrotate(a, d)

