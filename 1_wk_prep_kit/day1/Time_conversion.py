#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    nrm = s.lower()
    if "am" in nrm:
        time = nrm.split("am")[0]
        hr = time.split(":")
        if int(hr[0]) == 12:
            return f"00:{':'.join(hr[1:])}"
        else:
            return f"{':'.join(hr)}"

    elif "pm" in nrm:
        time = nrm.split("pm")[0]
        hr = time.split(":")
        if int(hr[0]) < 12:
            return f"{int(hr[0])+12}:{':'.join(hr[1:])}"
        else:
            return f"{':'.join(hr)}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
