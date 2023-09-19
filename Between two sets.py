#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' functi
on below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    result = 0 
    for i in range(max(a),min(b)+1):
        a_result = False 
        b_result = False 
        print('I',i)
        for a_res in a:
            print('a res',a_res)
            if i % a_res != 0:
                print('A break',i,a_res)
                a_result = False 
                break 
            a_result = True 
        print('A result',a_result)
        
        for b_res in b:
            print('b res',b_res)
            if b_res % i != 0:
                print('B break',b_res,i)
                b_result = False
                break
            b_result = True 
        print('B result',b_result)
        
        if a_result == True and b_result == True:
            result += 1 
        print('Result',result)
            
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
