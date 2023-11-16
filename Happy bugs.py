#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    if len(b) == 1:
        if b == '_':
            return 'YES'
        else:
            return 'NO'
            
    if '_' in b:
        if b.count('_') == len(b):
            return 'YES'
        
        return 'NO' if any(b.count(i) == 1 for i in b if i != '_') else 'YES'
        
    for i in range(len(b)):
        
        if i == 0 and b[i] != b[i+1]:
            return 'NO'
        elif i == len(b)-1 and b[i] != b[i-1]:
            return 'NO'
        elif b[i] != b[i-1] and b[i] != b[i+1]:
            return 'NO'
    return 'YES'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
