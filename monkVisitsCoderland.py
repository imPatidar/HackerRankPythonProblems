t=int(input())
for i in range(t):
    sum=0
    n=int(input())
    c=list(map(int,input().split()))
    l=list(map(int,input().split()))
    min=c[0]
    for j in range(n):
        if c[j]<min:
            min=c[j]
        sum+=min*l[j]
    print(sum)