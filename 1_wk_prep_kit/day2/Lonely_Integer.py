#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    if len(a) == 1:
        return a[0]
    for i in range(0, len(a)+1, 2):
        curr = a[i]
        if i != len(a)-1:
            nxt = a[i+1]
            if curr != nxt:
                return curr
        else:
            return curr




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
