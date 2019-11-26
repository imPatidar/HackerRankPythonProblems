# Enter your code here. Read input from STDIN. Print output to STDOUT

p,q = map(int, input().split())
pt = [('.|.'*(2*i + 1)).center(q, '-') for i in range(p//2)]
print('\n'.join(pt + ['WELCOME'.center(q,'-')] + pt[::-1]))