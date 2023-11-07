#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
import math 

def squares(a, b):
    # Write your code here
    res = []
    lower = math.ceil(math.sqrt(a))
    upper = math.floor(math.sqrt(b))
    
    for i in range(lower,upper+1):
        if i*i in range(a,b+1):
            res.append(i*i)
            
    print(res)
    return len(res)
    
    '''
    res = []
    for i in range(a,b+1):
        print('i --->',i)
        for j in range(1,(i//2)+1):
            print('j',j)
            if j*j == i:
                print('sqr',i)
                res.append(i)
    print(res)
    return len(res)
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
