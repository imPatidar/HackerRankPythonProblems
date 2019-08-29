# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations as p
a,b=input().split()
a=[char for char in a]
t=list(p(a,int(b)))
for i in sorted(t):
    print(''.join(list(i)))
