#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    dq = deque()
    
    for i in s:
        if len(dq) > 0 and dq[-1] == i:
            dq.pop()
        else:
            dq.append(i)
    
    if len(dq) > 0:
        return "".join(dq)
    else:
        return 'Empty String'
    
    # ls = list(s)
    # i = 0 
    
    # while i < len(ls)-1:
    #     if ls[i] == ls[i+1]:
    #         del ls[i]
    #         del ls[i]
    #         i = 0
    #         if len(ls) == 0:
    #             return 'Empty String'
    #     else: 
    #         i += 1 
    # return(''.join(ls))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
