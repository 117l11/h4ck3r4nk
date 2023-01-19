#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ttl = len(arr)
    pos = 0 # Positive
    neg = 0 # Negative
    zer = 0 # Zero

    for ar in arr:
        if ar > 0:
            pos +=1
        elif ar < 0:
            neg += 1
        else:
            zer +=1

    print(f"{pos/ttl:.6f}")
    print(f"{neg/ttl:.6f}")
    print(f"{zer/ttl:.6f}")



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
