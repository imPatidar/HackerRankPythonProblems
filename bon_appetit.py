#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    print(abs((sum(bill) - bill[k]) // 2 - b) if abs((sum(bill) - bill[k]) // 2 - b) else "Bon Appetit")


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
