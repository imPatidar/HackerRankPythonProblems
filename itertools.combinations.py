from itertools import combinations as c

a, b = input().split()
[print("".join(i)) for x in range(1,int(b)+1) for i in c(sorted(a),x) ]
