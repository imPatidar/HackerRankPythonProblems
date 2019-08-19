#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    t=scores[0]
    m=scores[0]
    p=0
    q=0
    for i in range(len(scores)):
        if(scores[i]<t):
            t=scores[i]
            p+=1
        elif(scores[i]>m):
            m=scores[i]
            q+=1
    return(q,p)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
