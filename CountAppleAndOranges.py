#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app=[]
    org=[]
    p=0
    q=0
    for i in apples:
        app.append(i+a)
    for i in oranges:
        org.append(i+b)
    for i in app:
        if(i>=s and i<=t):
            p+=1
    for j in org:
        if(j>=s and j<=t):
            q+=1
    print(str(p)+"\n"+str(q))



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
