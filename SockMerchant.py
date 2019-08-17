#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ur = set(ar)
    t=0
    for i in ur:
        t=t+ar.count(i)//2
    return t


ar=[1,1,3,2,2,4,2,4,1,1]
sockMerchant(3,ar)
