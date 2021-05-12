#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    num = 0 
    for i in range(len(B)):
        try:
            if B[i]%2 == 1:
                num +=2 
                B[i+1]+=1
        except:
            return "NO"
    return num 
            
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)
    
    if result == "NO":
        fptr.write(result + '\n')
    else:
        fptr.write(str(result) + '\n')

    #fptr.write(result + '\n')

    fptr.close()
