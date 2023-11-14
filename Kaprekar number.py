#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    res = []
    for i in range(p,q+1):
        l = str(i**2)[:(-len(str(i)))] or 0
        r = str(i**2)[(-len(str(i))):] or 0
        
        if int(float(l))+int(float(r)) == i:
            res.append(i)
            
    if len(res) == 0:
        print('INVALID RANGE')
    else: 
        print(*res)


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
